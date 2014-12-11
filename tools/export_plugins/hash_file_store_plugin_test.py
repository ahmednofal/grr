#!/usr/bin/env python
"""Tests for the hash file store export tool plugin."""


import argparse
import os

# pylint: disable=unused-import, g-bad-import-order
from grr.lib import server_plugins
# pylint: enable=unused-import, g-bad-import-order

from grr.lib import action_mocks
from grr.lib import aff4
from grr.lib import data_store
from grr.lib import flags
from grr.lib import flow
from grr.lib import rdfvalue
from grr.lib import test_lib
from grr.lib.hunts import output_plugins
from grr.tools.export_plugins import hash_file_store_plugin


class DummyOutputPlugin(output_plugins.HuntOutputPlugin):
  name = "dummy"

  responses = []

  def ProcessResponses(self, responses):
    DummyOutputPlugin.responses.extend(responses)


class HashFileStoreExportPluginTest(test_lib.GRRBaseTest):

  def setUp(self):
    super(HashFileStoreExportPluginTest, self).setUp()

    client_ids = self.SetupClients(1)
    self.client_id = client_ids[0]

    data_store.default_token = rdfvalue.ACLToken(username="user",
                                                 reason="reason")

  def testExportWithDummyPlugin(self):
    pathspec = rdfvalue.PathSpec(
        pathtype=rdfvalue.PathSpec.PathType.OS,
        path=os.path.join(self.base_path, "winexec_img.dd"))
    pathspec.Append(path="/Ext2IFS_1_10b.exe",
                    pathtype=rdfvalue.PathSpec.PathType.TSK)
    urn = aff4.AFF4Object.VFSGRRClient.PathspecToURN(pathspec, self.client_id)

    client_mock = action_mocks.ActionMock("TransferBuffer", "StatFile",
                                          "HashBuffer")
    for _ in test_lib.TestFlowHelper(
        "GetFile", client_mock, token=self.token,
        client_id=self.client_id, pathspec=pathspec):
      pass

    auth_state = rdfvalue.GrrMessage.AuthorizationState.AUTHENTICATED
    flow.Events.PublishEvent(
        "FileStore.AddFileToStore",
        rdfvalue.GrrMessage(payload=urn, auth_state=auth_state),
        token=self.token)
    worker = test_lib.MockWorker(token=self.token)
    worker.Simulate()

    plugin = hash_file_store_plugin.HashFileStoreExportPlugin()
    parser = argparse.ArgumentParser()
    plugin.ConfigureArgParser(parser)

    plugin.Run(parser.parse_args(args=[
        "--threads",
        "0",
        "dummy"
    ]))

    responses = DummyOutputPlugin.responses

    self.assertEqual(len(responses), 5)
    for response in responses:
      self.assertTrue(isinstance(response, rdfvalue.FileStoreHash))

    self.assertTrue(rdfvalue.FileStoreHash(
        fingerprint_type="pecoff", hash_type="md5",
        hash_value="a3a3259f7b145a21c7b512d876a5da06") in responses)
    self.assertTrue(rdfvalue.FileStoreHash(
        fingerprint_type="pecoff", hash_type="sha1",
        hash_value="019bddad9cac09f37f3941a7f285c79d3c7e7801") in responses)
    self.assertTrue(rdfvalue.FileStoreHash(
        fingerprint_type="generic", hash_type="md5",
        hash_value="bb0a15eefe63fd41f8dc9dee01c5cf9a") in responses)
    self.assertTrue(rdfvalue.FileStoreHash(
        fingerprint_type="generic", hash_type="sha1",
        hash_value="7dd6bee591dfcb6d75eb705405302c3eab65e21a") in responses)
    self.assertTrue(rdfvalue.FileStoreHash(
        fingerprint_type="generic", hash_type="sha256",
        hash_value="0e8dc93e150021bb4752029ebbff51394aa36f06"
        "9cf19901578e4f06017acdb5") in responses)


def main(argv):
  test_lib.main(argv)

if __name__ == "__main__":
  flags.StartMain(main)
