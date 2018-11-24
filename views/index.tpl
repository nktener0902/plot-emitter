<!DOCTYPE html>

<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Expression graph</title>

    <!-- Jquery -->
    <script   src="https://code.jquery.com/jquery-3.3.1.slim.js"   integrity="sha256-fNXJFIlca05BIO2Y5zh1xrShK3ME+/lYZ0j+ChxX2DA="   crossorigin="anonymous"></script>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

    <link rel="stylesheet" href="/stylesheet/index.css" type="text/css" />
    <link rel="stylesheet" href="/stylesheet/graph.css" type="text/css" />

    <!-- d3js -->
    <script src="https://d3js.org/d3.v3.min.js"></script>
    <!-- Custom JS -->
    <script type="text/javascript" src="/javascript/graph.js"></script>
    <script type="text/javascript" src="/javascript/index.js"></script>

</head>

<body>
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Expression viewer</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#about">About</a></li>
                <!-- <li><a href="/history">History</a></li> -->
                <li><a href="/logout">Logout</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container">
    <div class="starter-template">
        <div id="alert_message"></div>
        <form id="expression_input" action="/" method="post" accept-charset="utf-8">
            <p>
            <div class="input-group">
                <span class="input-group-addon" id="basic-addon1">y=</span>
                <input id="form_expression" class="form-control" value="{{expression}}" aria-describedby="basic-addon1" name="expression" type="text">
            </div>
            </p>
            <p>
                Noise function:
            <div class="dropdown">
                <button class="btn btn-default btn-sm dropdown-toggle" type="button" data-toggle="dropdown">
                    <span class="caret"></span>
                </button>
                <ul class="dropdown-menu">
                    <li><a href="#" data-value="none" onClick="noiseFuncEvent['none']();">None</a></li>
                    <li><a href="#" data-value="uniform" onClick="noiseFuncEvent['uniform']();">Uniform random</a></li>
                    <li><a href="#" data-value="gaussian" onClick="noiseFuncEvent['gaussian']();">Gaussian noise</a></li>
                </ul>
                <input id="dropdown_noise_function" type="hidden" name="noise_function" value="">
            </div>
            </p>
            <p>
            <div id="noise_div">
                <span id="noise_span">&nbsp;&nbsp;&nbsp;Noise: </span>
                <input id="form_noise" value="{{noise}}" name="noise" type="text">
            </div>
            </p>
            <p>Interval of X plots:
                <input id="form_fineness" value="{{fineness}}" name="fineness" type="text">
            </p>
            <p>X axis range:&nbsp;&nbsp;
                <input id="form_x_min_range" value="{{x_min_range}}" name="x_min_range" type="text"> &le; x &le;
                <input id="form_x_max_range" value="{{x_max_range}}" name="x_max_range" type="text">
            </p>
            <p>
            <div class="input-group">
                <span class="input-group-addon" id="basic-addon1">Comment</span>
                <input id="form_comment" value="{{comment}}" class="form-control" aria-describedby="basic-addon1" name="comment" type="text">
            </div>
            </p>
            <button class="btn btn-lg btn-primary" type="submit" onclick="document.charset='utf-8';">Output</button>
        </form>
        <hr />

        %if len(plots) != 0:
        <div>
            <p>Expression: y = {{expression}}</p>
            <p>Noise function: {{noise_function}}</p>
            <p>Noise: {{noise}}</p>
            <p>Interval of X plots: {{fineness}}</p>
            <p>{{x_min_range}} &le; x &le; {{x_max_range}}</p>
            <p>{{comment}}</p>
            <svg id="graph"></svg>
            <script type="text/javascript">
                createsvg("{{plots}}");
            </script>
        </div>
        <!-- <div>
            <button class="btn btn-lg btn-success" onclick="tableDownload({{plots}})">Download</button>
        </div> -->
        %end
        <table class="table table-striped">
            <thead>
            <tr><th>x</th><th>y</th></tr>
            </thead>
            <tbody>
            %for plot in plots:
            %px = str(plot["x"])
            %pf = str(plot["f"])
            <tr><th>{{px}}</th><th>{{pf}}</th></tr>
            %end
            </tbody>
        </table>
    </div>
</div>

<!-- Latest compiled and minified JavaScript -->
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<!-- Custom JavaScript -->
%if message != "":
<script type="text/javascript">alertSetShow("{{message}}");</script>
%end

</body>
</html>
