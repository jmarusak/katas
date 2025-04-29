package graphs;

import org.neo4j.driver.AuthTokens;
import org.neo4j.driver.GraphDatabase;

public class App {

    public static void main(String... args) {

        // URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
        final String dbUri = "bolt://localhost:7687";
        final String dbUser = "neo4j";
        final String dbPassword = "secretgraph";

        try (var driver = GraphDatabase.driver(dbUri, AuthTokens.basic(dbUser, dbPassword))) {
            driver.verifyConnectivity();
            System.out.println("Connection established.");
        }
    }
}
