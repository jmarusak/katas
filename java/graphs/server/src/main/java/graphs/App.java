package graphs;

import java.io.IOException;
import java.nio.file.Path;

import org.neo4j.configuration.connectors.BoltConnector;
import org.neo4j.configuration.connectors.HttpConnector;
import org.neo4j.configuration.helpers.SocketAddress;

import org.neo4j.dbms.api.DatabaseManagementService;
import org.neo4j.dbms.api.DatabaseManagementServiceBuilder;
import org.neo4j.graphdb.GraphDatabaseService;
import org.neo4j.graphdb.Transaction;
import org.neo4j.graphdb.Label;
import org.neo4j.graphdb.Node;

import static org.neo4j.configuration.GraphDatabaseSettings.DEFAULT_DATABASE_NAME;

public class App {
    private static final Path databaseDirectory = Path.of("target/neo4j-db");

    public static void main(String[] args) throws IOException {

        // Configure the database management service
        DatabaseManagementService managementService = new DatabaseManagementServiceBuilder(databaseDirectory)
                .setConfig(HttpConnector.enabled, true)
                .setConfig(HttpConnector.listen_address, new SocketAddress("localhost", 7474))
                .setConfig(BoltConnector.enabled, true)
                .setConfig(BoltConnector.listen_address, new SocketAddress("localhost", 7687))
                .build();

        // Start the database
        GraphDatabaseService graphDb = managementService.database(DEFAULT_DATABASE_NAME);

        // Register a shutdown hook
        registerShutdownHook(managementService);

        try (Transaction tx = graphDb.beginTx()) {
            // Create a node
            Node node = tx.createNode(Label.label("Person"));
            node.setProperty("name", "John Doe");
            tx.commit();
        }
    }

    private static void registerShutdownHook(final DatabaseManagementService managementService) {
        // Registers a shutdown hook for the Neo4j instance so that it
        // shuts down nicely when the VM exits (even if you "Ctrl-C" the
        // running application).
        Runtime.getRuntime().addShutdownHook(new Thread() {
            @Override
            public void run() {
                managementService.shutdown();
            }
        });
    }
}
