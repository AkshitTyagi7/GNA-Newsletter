import time

from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED
from cassandra.policies import WhiteListRoundRobinPolicy, DowngradingConsistencyRetryPolicy, ConsistencyLevel
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import BatchStatement, SimpleStatement, BatchType
import yaml




class keyspace_connect():

    def __init__(self):
        self.credentials = {}
        self.decode_yaml()
        self.cluster = self.cassandra_connect()
        fl = 0
        while fl!=1:
            try:
                self.cass_session = self.cluster.connect()
                fl=1
            except:
                fl=0
                time.sleep(1)

    def cassandra_connect(self):
        profile = ExecutionProfile(
            retry_policy=DowngradingConsistencyRetryPolicy(),
            consistency_level=ConsistencyLevel.LOCAL_QUORUM,
            serial_consistency_level=ConsistencyLevel.LOCAL_SERIAL,
            request_timeout=15,
        )
        ssl_context = SSLContext(PROTOCOL_TLSv1_2)
        ssl_context.load_verify_locations('sf-class2-root.crt')
        ssl_context.verify_mode = CERT_REQUIRED
        auth_provider = PlainTextAuthProvider(username=self.credentials['production']['keyspaces']['user'],
                                              password=self.credentials['production']['keyspaces']['password'])
        cluster = Cluster([self.credentials['production']['keyspaces']['cluster']], ssl_context=ssl_context,
                          auth_provider=auth_provider,
                          port=self.credentials['production']['keyspaces']['port'],
                          execution_profiles={EXEC_PROFILE_DEFAULT: profile})

        return cluster

    def decode_yaml(self):
        file_path = 'config.yml'

        with open(file_path, 'r') as file:
            self.credentials = yaml.safe_load(file)

    def execute_query(self, query):
        self.cass_session
        return list(self.cass_session.execute(query))


DataExtraction = keyspace_connect()

