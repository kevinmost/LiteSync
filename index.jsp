<!DOCTYPE html>
<%@ page import="java.net.*" %>
<%@ page import="java.io.*" %>
<%@ page import="twitter4j.Query,twitter4j.QueryResult,twitter4j.Status,twitter4j.Twitter,twitter4j.TwitterException,twitter4j.TwitterFactory,twitter4j.conf.ConfigurationBuilder,de.tudarmstadt.*" %>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">

		<title>Twitsaurus Beta</title>

		<!-- Bootstrap core CSS -->
		<link href="css/bootstrap.css" rel="stylesheet">

		<!-- Custom styles for this template -->
		<link href="css/style.css" rel="stylesheet">

		<!-- Just for debugging purposes. Don't actually copy this line! -->
		<!--[if lt IE 9]><script src="../../docs-assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

		<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
			<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
			<script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
		<![endif]-->
	</head>

	<body>
		<!-- Fixed navbar -->
		<div class="navbar navbar-default navbar-fixed-top" role="navigation">
			<div class="container">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
						<span class="sr-only">Toggle navigation</span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</button>
					<a class="navbar-brand" href="#">Twitsaurus Beta</a>
					<form class="navbar-form navbar-right" role="form" action="index.jsp" method="GET">
						<div class="form-group">
							<input type="text" placeholder="Enter text to search" class="form-control" name="search">
						</div>
						<div class="form-group">
							<input type="checkbox" name="random" value="Random">Random image?</input>
						</div>
						<button type="submit" value="Submit" class="btn btn-success">Search!</button>
					</form>
				</div>
			</div>
		</div>
		<div>
			<!-- Main component for a primary marketing message or call to action -->
			<div class="col-xs-5" id="column-twitter">
				<h2>Here's what people on Twitter are saying about <strong>"<%= request.getParameter("search") %>"</strong></h2>
				<%
					if (request.getParameter("search") !=  null) {
						ConfigurationBuilder cb = new ConfigurationBuilder();
						cb.setDebugEnabled(true)
						  .setOAuthConsumerKey("IumnEae0GIvKylSsJPbjA")
						  .setOAuthConsumerSecret("uXs22bo5zDCeX18ax5Fq4IgNxJbVmdJpShXvYUCD8")
						  .setOAuthAccessToken("2228768737-pqYhT8oJd7b6lRmznmGrgGphm9Jw5ePJ8TQnxf2")
						  .setOAuthAccessTokenSecret("SD0JwlGvOb9kipB4Bgom5E7p4j379mzArTRnNU4jEmKrD");
						TwitterFactory tf = new TwitterFactory(cb.build());
					
						Twitter twitter = tf.getInstance();
						
						Query query = new Query(request.getParameter("search"));
						QueryResult result = twitter.search(query);
						for (Status status : result.getTweets()) {
							out.println("<strong>@" + status.getUser().getScreenName() + ":</strong>" + status.getText());
							out.println("<br />");
						}
					}
				%>
			</div>

			<div class="col-xs-5" id="column-picture">			
				<h2>Here is a picture of <strong>"<%= request.getParameter("search") %>"</strong></h2>
				<% 
					if (request.getParameter("search") != null) {
						String random = "";
						if (request.getParameter("random") != null) {
							if (request.getParameter("random").equals("Random")) {
								random = "r";
							}
						}
						String picureSource = new BufferedReader(new InputStreamReader(new URL("http://" + request.getParameter("search").replaceAll("\\s","") + ".jpg.to/" + random).openStream())).readLine();
						out.println(picureSource.replaceAll("(?<=img )(.*)(?=src)", ""));
					}
				%>


			</div>

			<div class="col-xs-2" id="column-definition">
				<h2>Here is the definition of <strong>"<%= request.getParameter("search") %>"</strong></h2>
				<%
					if (request.getParameter("search") != null) {
						URL url = new URL("http://www.thefreedictionary.com/p/" + request.getParameter("search").replaceAll("\\s",""));
						URLConnection spoof = url.openConnection();
						
						spoof.setRequestProperty( "User-Agent", "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; H010818)" );
						BufferedReader in = new BufferedReader(new InputStreamReader(spoof.getInputStream()));
						String strLine = "";
						String definitionSource = "";
						while ((strLine = in.readLine()) != null){
							definitionSource += strLine + "\n";
						}
						
						String startDelimiter = "<div class=\"ds-single\">";
						if (definitionSource.contains(startDelimiter)) {
							definitionSource = definitionSource.substring(definitionSource.indexOf(startDelimiter));
							definitionSource = definitionSource.substring(startDelimiter.length(), definitionSource.indexOf("</div>"));
							out.println(definitionSource);
						}
						else {
							out.println("No definition found");
						}
					}
				%>
			</div>
		</div>

		<div id="footer">
			<h2><a href="http://www.ivefinancial.com/inc/store/store_eCommerce.php?id_corp=11777">BUY AD SPACE</a></h2>
		</div>
		


		<!-- Bootstrap core JavaScript
		================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/javascript.js"></script>
	</body>
</html>
