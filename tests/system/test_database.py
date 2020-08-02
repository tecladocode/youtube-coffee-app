import unittest
import sqlite3
import database


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = database.connect(":memory:")

    def test_database_creates_tables(self):
        database.create_tables(self.connection)

        with self.connection:
            self.connection.execute("SELECT * FROM beans;")

    def test_database_insert_beans(self):
        database.create_tables(self.connection)
        database.add_bean(self.connection, "Test Bean", "Percolator", 100)

        with self.connection:
            cursor = self.connection.execute("SELECT * FROM beans;")
            results = cursor.fetchone()
            self.assertEqual(results[1], "Test Bean")
            self.assertEqual(results[2], "Percolator")
            self.assertEqual(results[3], 100)

    def test_get_all_beans(self):
        database.create_tables(self.connection)
        database.add_bean(self.connection, "Test Bean", "Percolator", 100)
        beans = database.get_all_beans(self.connection)

        self.assertEqual(beans[0][1], "Test Bean")
        self.assertEqual(beans[0][2], "Percolator")
        self.assertEqual(beans[0][3], 100)

    def test_get_beans_by_name(self):
        database.create_tables(self.connection)
        database.add_bean(self.connection, "Test Bean", "Percolator", 100)
        beans = database.get_beans_by_name(self.connection, "Test Bean")

        self.assertEqual(beans[0][1], "Test Bean")

    def test_get_multiple_beans_by_name(self):
        database.create_tables(self.connection)
        database.add_bean(self.connection, "Test Bean", "Percolator", 100)
        database.add_bean(self.connection, "Test Bean", "Espresso", 80)
        beans = database.get_beans_by_name(self.connection, "Test Bean")

        self.assertEqual(beans[0][1], "Test Bean")
        self.assertEqual(beans[1][1], "Test Bean")
        self.assertEqual(beans[0][2], "Percolator")
        self.assertEqual(beans[1][2], "Espresso")

    def test_get_best_preparation_for_bean(self):
        database.create_tables(self.connection)
        database.add_bean(self.connection, "Test Bean", "Percolator", 100)
        database.add_bean(self.connection, "Test Bean", "Espresso", 80)
        best_preparation = database.get_best_preparation_for_bean(self.connection, "Test Bean")

        self.assertEqual(best_preparation[2], "Percolator")


if __name__ == '__main__':
    unittest.main()
