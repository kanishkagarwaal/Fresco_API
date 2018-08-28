from views.api import app
import unittest
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

class TestIntegrations(unittest.TestCase):



	def test_connection(self):
		cluster = Cluster()
		session = cluster.connect(keyspace="fresco_seg")
		print (str(cluster.port))
		self.assertEqual(cluster.port, 9042)

		
if __name__ == "__main__":
	unittest.main()