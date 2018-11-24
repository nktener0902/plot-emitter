%# This is login page.

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

    <link rel="stylesheet" href="/stylesheet/home.css" type="text/css" />
    <link rel="stylesheet" href="/stylesheet/login.css" type="text/css" />

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
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container">
    <div class="starter-template">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <div class="login_alert"></div>
                %if not nomatch == "":
                <div class="alert">
                    <span class="closebtn" onclick="this.parentElement.style.display='none';"> x </span>
                    <p>{{nomatch}}</p>
                </div>
                %end
                <ul class="tab">
                    <li>
                        <a id="defaultOpen" href="javascript:void(0)" class="tablinks" onclick="openTab(event, 'Login')"> Login </a>
                    </li>
                    <li>
                        <a href="javascript:void(0)" class="tablinks" onclick="openTab(event, 'Register')"> Register </a>
                    </li>
                </ul>
                <div id="Login" class="tabcontent">
                    <h2>Log in</h2>
                    <form action="/login" method="POST">
                        <div class="form-group">
                            <input id="loginform" type="text", name="email", placeholder="Email">
                        </div>
                        <div class="form-group">
                            <input id="loginform" type="password", name="password", placeholder="Password">
                        </div>
                        <div class="form-group">
                            <button id="login_button" class="btn btn-success" type="submit">Log in</button>
                        </div>
                    </form>
                </div>
                <div id="Register" class="tabcontent">
                    <h2>Register</h2>
                    <form action="/register" method="POST">
                        <div class="form-group">
                            <input id="loginform" type="text", name="email", placeholder="Email">
                        </div>
                        <div class="form-group">
                            <input id="loginform" type="password", name="password", placeholder="Password">
                        </div>
                        <div class="form-group">
                            <button id="register_button" class="btn btn-success" type="submit">Create account</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Latest compiled and minified JavaScript -->
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>


<!-- Custom JS -->
<script type="text/javascript" src="/javascript/logintab.js"></script>

</body>
</html>
