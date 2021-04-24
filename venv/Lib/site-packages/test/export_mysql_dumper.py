# coding: utf-8
from unittest import TestCase
import six
from codecs import open
from tools.encoding import make_str
from tools.export.mysql_dumper import MysqlCSVDumper, build_import_sql
from tempfile import mkstemp
import os

IMPORT_SQL = r'''LOAD DATA LOCAL INFILE "/tmp/x.sql"
REPLACE INTO TABLE foo
character set utf8
fields terminated by "," optionally enclosed by '"'
lines terminated by "\r\n"
(col1,col2);'''

class MysqlCSVDumperTestCase(TestCase):
    def test_constructor(self):
        fh, path = mkstemp()
        MysqlCSVDumper(path)
        os.unlink(path)

    def test_normalize_none_value(self):
        fh, path = mkstemp()
        dumper = MysqlCSVDumper(path)
        dumper.add_row((None,))
        dumper.close()
        self.assertTrue(r'\N' in open(path, encoding='utf-8').read())
        os.unlink(path)

    def test_normalize_unicode(self):
        fh, path = mkstemp()
        dumper = MysqlCSVDumper(path)
        dumper.add_row((u'фуу',))
        dumper.close()
        self.assertTrue(u'фуу' in open(path, encoding='utf-8').read())
        os.unlink(path)

    def test_normalize_bytes(self):
        fh, path = mkstemp()
        dumper = MysqlCSVDumper(path)
        dumper.add_row((make_str('фуу'),))
        dumper.close()
        self.assertTrue(u'фуу' in open(path, encoding='utf-8').read())
        os.unlink(path)

    def test_normalize_int(self):
        fh, path = mkstemp()
        dumper = MysqlCSVDumper(path)
        dumper.add_row((1,))
        dumper.close()
        self.assertTrue(u'1' in open(path, encoding='utf-8').read())
        os.unlink(path)

    def test_build_import_sql(self):
        self.assertEqual(
            IMPORT_SQL, build_import_sql('/tmp/x.sql', 'foo', ['col1', 'col2']))
