#
# ovirt-engine-setup -- ovirt engine setup
# Copyright (C) 2013-2015 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""DWH Constants."""


import os
import gettext


from otopi import util

from ovirt_engine_setup.constants import classproperty
from ovirt_engine_setup.constants import osetupattrsclass
from ovirt_engine_setup.constants import osetupattrs
from ovirt_engine_setup.engine_common import constants as oengcommcons


from . import config


def _(m):
    return gettext.dgettext(message=m, domain='ovirt-engine-dwh')


DEK = oengcommcons.DBEnvKeysConst


@util.export
@util.codegen
class Const(object):
    PACKAGE_NAME = config.PACKAGE_NAME
    PACKAGE_VERSION = config.PACKAGE_VERSION
    DISPLAY_VERSION = config.DISPLAY_VERSION
    RPM_VERSION = config.RPM_VERSION
    RPM_RELEASE = config.RPM_RELEASE
    VERSION_MAJOR = config.VERSION_MAJOR
    VERSION_MINOR = config.VERSION_MINOR
    VERSION_PATCH_LEVEL = config.VERSION_PATCH_LEVEL
    SERVICE_NAME = 'ovirt-engine-dwhd'
    OVIRT_ENGINE_DWH_DB_BACKUP_PREFIX = 'dwh'
    OVIRT_ENGINE_DWH_PACKAGE_NAME = 'ovirt-engine-dwh'
    OVIRT_ENGINE_DWH_SETUP_PACKAGE_NAME = 'ovirt-engine-dwh-setup'

    @classproperty
    def DWH_DB_ENV_KEYS(self):
        return {
            DEK.HOST: DBEnv.HOST,
            DEK.PORT: DBEnv.PORT,
            DEK.SECURED: DBEnv.SECURED,
            DEK.HOST_VALIDATION: DBEnv.SECURED_HOST_VALIDATION,
            DEK.USER: DBEnv.USER,
            DEK.PASSWORD: DBEnv.PASSWORD,
            DEK.DATABASE: DBEnv.DATABASE,
            DEK.CONNECTION: DBEnv.CONNECTION,
            DEK.PGPASSFILE: DBEnv.PGPASS_FILE,
            DEK.NEW_DATABASE: DBEnv.NEW_DATABASE,
            DEK.DUMPER: DBEnv.DUMPER,
            DEK.FILTER: DBEnv.FILTER,
            DEK.RESTORE_JOBS: DBEnv.RESTORE_JOBS,
        }

    @classproperty
    def DEFAULT_DWH_DB_ENV_KEYS(self):
        return {
            DEK.HOST: Defaults.DEFAULT_DB_HOST,
            DEK.PORT: Defaults.DEFAULT_DB_PORT,
            DEK.SECURED: Defaults.DEFAULT_DB_SECURED,
            DEK.HOST_VALIDATION: Defaults.DEFAULT_DB_SECURED_HOST_VALIDATION,
            DEK.USER: Defaults.DEFAULT_DB_USER,
            DEK.PASSWORD: Defaults.DEFAULT_DB_PASSWORD,
            DEK.DATABASE: Defaults.DEFAULT_DB_DATABASE,
            DEK.DUMPER: Defaults.DEFAULT_DB_DUMPER,
            DEK.FILTER: Defaults.DEFAULT_DB_FILTER,
            DEK.RESTORE_JOBS: Defaults.DEFAULT_DB_RESTORE_JOBS,
        }


@util.export
@util.codegen
class Defaults(object):
    DEFAULT_DB_HOST = 'localhost'
    DEFAULT_DB_PORT = 5432
    DEFAULT_DB_DATABASE = 'ovirt_engine_history'
    DEFAULT_DB_USER = 'ovirt_engine_history'
    DEFAULT_DB_PASSWORD = ''
    DEFAULT_DB_SECURED = False
    DEFAULT_DB_SECURED_HOST_VALIDATION = False
    DEFAULT_DB_DUMPER = 'pg_custom'
    DEFAULT_DB_RESTORE_JOBS = 2
    DEFAULT_DB_FILTER = None


@util.export
@util.codegen
class FileLocations(object):
    PKG_SYSCONF_DIR = config.PKG_SYSCONF_DIR
    PKG_STATE_DIR = config.PKG_STATE_DIR
    PKG_DATA_DIR = config.PKG_DATA_DIR
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG = \
        config.OVIRT_ENGINE_DWHD_SERVICE_CONFIG
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_DEFAULTS = \
        config.OVIRT_ENGINE_DWHD_SERVICE_CONFIG_DEFAULTS
    OVIRT_ENGINE_DWHD_SERVICE_CONFIGD = '%s.d' % \
        OVIRT_ENGINE_DWHD_SERVICE_CONFIG
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_DATABASE = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '10-setup-database.conf',
    )
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_UUID = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '10-setup-uuid.conf',
    )
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_SCALE = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '10-setup-scale.conf',
    )
    OVIRT_ENGINE_DWHD_SERVICE_CONFIG_LEGACY = os.path.join(
        OVIRT_ENGINE_DWHD_SERVICE_CONFIGD,
        '20-setup-legacy.conf',
    )

    # sync with engine
    OVIRT_ENGINE_ENGINE_SERVICE_CONFIGD = '/etc/ovirt-engine/engine.conf.d'
    OVIRT_ENGINE_ENGINE_SERVICE_CONFIG_DATABASE = os.path.join(
        OVIRT_ENGINE_ENGINE_SERVICE_CONFIGD,
        '10-setup-database.conf'
    )
    OVIRT_ENGINE_ENGINE_SERVICE_CONFIG_DWH_DATABASE = os.path.join(
        OVIRT_ENGINE_ENGINE_SERVICE_CONFIGD,
        '10-setup-dwh-database.conf'
    )

    # should have same basename as
    # OVIRT_ENGINE_ENGINE_SERVICE_CONFIG_DWH_DATABASE, to make it easier
    # to trace etc.
    OVIRT_ENGINE_ENGINE_SERVICE_CONFIG_DWH_DATABASE_EXAMPLE = os.path.join(
        PKG_SYSCONF_DIR,
        'examples',
        '10-setup-dwh-database.conf'
    )

    OVIRT_ENGINE_DWH_DB_DIR = os.path.join(
        PKG_DATA_DIR,
        'dbscripts',
    )
    OVIRT_ENGINE_DWH_DB_SCHMA_TOOL = os.path.join(
        OVIRT_ENGINE_DWH_DB_DIR,
        'schema.sh',
    )
    OVIRT_ENGINE_DEFAULT_DWH_DB_BACKUP_DIR = os.path.join(
        PKG_STATE_DIR,
        'backups',
    )

    OVIRT_ENGINE_DB_MD5_DIR = os.path.join(
        PKG_STATE_DIR,
        'dwh_dbmd5',
    )

    LEGACY_CONFIG = os.path.join(
        PKG_SYSCONF_DIR,
        '..',
        'ovirt-engine',
        'ovirt-engine-dwh',
        'Default.properties',
    )


@util.export
class Stages(object):
    CORE_ENABLE = 'osetup.dwh.core.enable'
    DB_CONNECTION_SETUP = 'osetup.dwh.db.connection.setup'
    DB_CREDENTIALS_AVAILABLE = 'osetup.dwh.db.connection.credentials'
    DB_CONNECTION_CUSTOMIZATION = 'osetup.dwh.db.connection.customization'
    DB_CONNECTION_AVAILABLE = 'osetup.dwh.db.connection.available'
    ENGINE_DB_CONNECTION_AVAILABLE = \
        'osetup.dwh.engine.db.connection.available'
    DB_SCHEMA = 'osetup.dwh.db.schema'


@util.export
@util.codegen
@osetupattrsclass
class CoreEnv(object):

    @osetupattrs(
        answerfile=True,
        postinstallfile=True,
        summary=True,
        reconfigurable=True,
        description=_('DWH installation'),
    )
    def ENABLE(self):
        return 'OVESETUP_DWH_CORE/enable'

    UUID = 'OVESETUP_DWH_CORE/uuid'


@util.export
@util.codegen
@osetupattrsclass
class ConfigEnv(object):

    @osetupattrs(
        answerfile=True,
    )
    def OVIRT_ENGINE_DWH_DB_BACKUP_DIR(self):
        return 'OVESETUP_DWH_CONFIG/dwhDbBackupDir'

    DWH_SERVICE_STOP_NEEDED = 'OVESETUP_DWH_CONFIG/dwhServiceStopNeeded'

    @osetupattrs(
        postinstallfile=True,
    )
    def REMOTE_ENGINE_CONFIGURED(self):
        return 'OVESETUP_DWH_CONFIG/remoteEngineConfigured'

    @osetupattrs(
        answerfile=True,
        postinstallfile=True,
    )
    def SCALE(self):
        return 'OVESETUP_DWH_CONFIG/scale'


@util.export
@util.codegen
@osetupattrsclass
class DBEnv(object):

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database host'),
    )
    def HOST(self):
        return 'OVESETUP_DWH_DB/host'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database port'),
    )
    def PORT(self):
        return 'OVESETUP_DWH_DB/port'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database secured connection'),
    )
    def SECURED(self):
        return 'OVESETUP_DWH_DB/secured'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database host name validation'),
    )
    def SECURED_HOST_VALIDATION(self):
        return 'OVESETUP_DWH_DB/securedHostValidation'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database name'),
    )
    def DATABASE(self):
        return 'OVESETUP_DWH_DB/database'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('DWH database user name'),
    )
    def USER(self):
        return 'OVESETUP_DWH_DB/user'

    @osetupattrs(
        answerfile=True,
        answerfile_condition=lambda env: not env.get(
            ProvisioningEnv.POSTGRES_PROVISIONING_ENABLED
        ),
    )
    def PASSWORD(self):
        return 'OVESETUP_DWH_DB/password'

    @osetupattrs(
        answerfile=True,
    )
    def DUMPER(self):
        return 'OVESETUP_DWH_DB/dumper'

    @osetupattrs(
        answerfile=True,
    )
    def FILTER(self):
        return 'OVESETUP_DWH_DB/filter'

    @osetupattrs(
        answerfile=True,
    )
    def RESTORE_JOBS(self):
        return 'OVESETUP_DWH_DB/restoreJobs'

    CONNECTION = 'OVESETUP_DWH_DB/connection'
    STATEMENT = 'OVESETUP_DWH_DB/statement'
    PGPASS_FILE = 'OVESETUP_DWH_DB/pgPassFile'
    NEW_DATABASE = 'OVESETUP_DWH_DB/newDatabase'

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('Backup DWH database'),
    )
    def PERFORM_BACKUP(self):
        return 'OVESETUP_DWH_DB/performBackup'

    @osetupattrs(
        answerfile=True,
    )
    def RESTORE_BACKUP_LATE(self):
        return 'OVESETUP_DWH_DB/restoreBackupLate'

    @osetupattrs(
        answerfile=True,
    )
    def DISCONNECT_EXISTING_DWH(self):
        return 'OVESETUP_DWH_DB/disconnectExistingDwh'


@util.export
@util.codegen
@osetupattrsclass
class RemoveEnv(object):
    @osetupattrs(
        answerfile=True,
    )
    def REMOVE_DATABASE(self):
        return 'OVESETUP_DWH_REMOVE/database'


@util.export
@util.codegen
@osetupattrsclass
class ProvisioningEnv(object):

    @osetupattrs(
        answerfile=True,
        summary=True,
        description=_('Configure local DWH database'),
    )
    def POSTGRES_PROVISIONING_ENABLED(self):
        return 'OVESETUP_DWH_PROVISIONING/postgresProvisioningEnabled'


@util.export
@util.codegen
@osetupattrsclass
class RPMDistroEnv(object):
    PACKAGES = 'OVESETUP_DWH_RPMDISRO_PACKAGES'
    PACKAGES_SETUP = 'OVESETUP_DWH_RPMDISRO_PACKAGES_SETUP'


# vim: expandtab tabstop=4 shiftwidth=4
