# Search-Engine-for-Historical-Aritfacts

Technology: Apache Nutch, python, java servlets, web UI (HTML, CSS, jQuery, javaScript, Apache Tomcat server)

Worked in a team of 5 members (Please check report for details about individual member contribution)

1. I was responsible for the crawling process of approx. 200,000 webpages which is used for creating the index of URLS.

2. Crawling was done using both Apache Nutch with Solr indexer as well using Python web crawler scripts.

3. The index was created using the Solr indexer and Apache Lucene library.

4. Vector space relevance model and Page Ranking and HITS algorithms were implemented using python API.

5. The web UI was created using HTML, CSS, javaScript, jQuery and Java servlets to handle all the API calls and was hosted on Apache Tomcat server. The results from indexing , clustering and query expansion were all displayed on the UI.

6. Flat clustering (K-means) and Agglomerative clustering techniques were programmed using python scripts and hosed on a local python server.

7. Java Springboot was used to deploy the query expansion algorithm scripts (Rocchio algorithm, scalar, association and metric clusters) on to the local server and integrate with UI to show the expanded queries.
