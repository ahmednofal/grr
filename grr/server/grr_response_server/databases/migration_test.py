#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import os

from absl.testing import absltest
import mock

from grr_response_core import config
from grr_response_core.lib import flags
from grr_response_core.lib.rdfvalues import artifacts as rdf_artifacts
from grr_response_server import artifact_registry
from grr_response_server import data_store
from grr_response_server import db
from grr_response_server.databases import mem
from grr_response_server.databases import migration
from grr.test_lib import test_lib


def _SetUpArtifacts():
  test_artifacts_file = os.path.join(config.CONFIG["Test.data_dir"],
                                     "artifacts", "test_artifacts.json")
  artifact_registry.REGISTRY.AddFileSource(test_artifacts_file)


class ArtifactMigrationTest(absltest.TestCase):

  def setUp(self):
    super(ArtifactMigrationTest, self).setUp()

    self._db_patcher = mock.patch.object(
        data_store, "REL_DB", db.DatabaseValidationWrapper(mem.InMemoryDB()))
    self._db_patcher.start()

    self._artifact_patcher = mock.patch.object(
        artifact_registry, "REGISTRY", artifact_registry.ArtifactRegistry())
    self._artifact_patcher.start()

  def tearDown(self):
    self._db_patcher.stop()
    self._artifact_patcher.stop()
    super(ArtifactMigrationTest, self).tearDown()

  @mock.patch.object(data_store, "RelationalDBReadEnabled", return_value=False)
  @mock.patch.object(migration, "_IsCustom", return_value=True)
  def testMigratesAllArtifactsWithoutReadFromRelDB(self, *unused_mocks):
    self.assertEmpty(data_store.REL_DB.ReadAllArtifacts())
    _SetUpArtifacts()
    self.assertEmpty(data_store.REL_DB.ReadAllArtifacts())
    migration.MigrateArtifacts()
    self.assertLen(data_store.REL_DB.ReadAllArtifacts(), 29)

  @mock.patch.object(data_store, "RelationalDBReadEnabled", return_value=True)
  @mock.patch.object(migration, "_IsCustom", return_value=True)
  def testMigratesAllArtifactsWithReadFromRelDB(self, *unused_mocks):
    self.assertEmpty(data_store.REL_DB.ReadAllArtifacts())
    _SetUpArtifacts()
    self.assertEmpty(data_store.REL_DB.ReadAllArtifacts())
    migration.MigrateArtifacts()
    self.assertLen(data_store.REL_DB.ReadAllArtifacts(), 29)

  def testDeletesExistingArtifactsInRelDB(self):
    data_store.REL_DB.WriteArtifact(rdf_artifacts.Artifact(name="old"))
    self.assertLen(data_store.REL_DB.ReadAllArtifacts(), 1)
    migration.MigrateArtifacts()
    self.assertEmpty(data_store.REL_DB.ReadAllArtifacts())


def main(args):
  test_lib.main(args)


if __name__ == "__main__":
  flags.StartMain(main)
