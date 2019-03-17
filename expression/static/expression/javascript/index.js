var alert_message = "";

var popupMessage = function(){
    alertAutoSet();
    alertShow();
    if (alert_message != ""){
        return false;
    }
}

var alertAutoSet = function() {
    alert_message = "";
    var expression = document.getElementById('form_expression');
    var noise_function = document.getElementById('dropdown_noise_function');
    var noise = document.getElementById('form_noise');
    var fineness = document.getElementById('form_fineness');
    var x_min_range = document.getElementById('form_x_min_range');
    var x_max_range = document.getElementById('form_x_max_range');
    if (expression.value == '' ||
        noise_function.value == '' ||
        fineness.value == '' ||
        x_min_range.value == '' ||
        x_max_range.value == ''){
        alert_message = "Please fill out all forms.";
    } else if (noise_function.value != 'none' && noise.value == ''){
        alert_message = "Please fill out all forms.";
    } else if (noise_function.value != 'none' && isNaN(filterFloat(noise.value))){
        alert_message = "Invalid data type. Noise is int or float.";
    } else if (isNaN(filterFloat(fineness.value))){
        alert_message = "Invalid data type. Fineness is int or float.";
    } else if (isNaN(filterFloat(x_min_range.value) || isNaN(filterFLoat(x_max_range.ralue)))){
        alert_message = "Invalid data type. X axis range is int or float.";
    } else if (parseFloat(x_min_range.value) > parseFloat(x_max_range.value)){
        alert_message = "Max of x-axis range has to be more than min of x-axis range.";
    } else if (parseFloat(fineness.value) == 0){
        alert_message = "Fineness is not allowed to be '0'.";
    }
}

var alertSet = function(msg){
    alert_message = msg;
}

var alertSetShow = function(msg){
    alert_message = msg;
    alertShow();
}

var alertShow = function(){
    if (alert_message != ""){
        var alert = document.getElementById('alert_message');
        var div = document.createElement('div');
        div.setAttribute('id', 'alert');
        while (alert.firstChild) alert.removeChild(alert.firstChild);
        var span = document.createElement('span');
        span.setAttribute('class', 'closebtn');
        span.setAttribute('onclick', 'this.parentElement.style.display="none";');
        span.textContent = "x";
        var message = document.createElement('p');
        message.textContent = alert_message;
        div.appendChild(span);
        div.appendChild(message);
        alert.appendChild(div);
    }
}

var filterInt = function(value){
    if(/^(\-|\+)?[0-9]+$/.test(value)) {
        return Number(value);
    }
    return NaN;
}

var filterFloat = function(value){
    if(/^(\-|\+)?([0-9]+(\.[0-9]+)?)$/.test(value)) {
        return Number(value);
    }
    return NaN;
}

$(function(){
    $(".dropdown-menu li a").click(function(){
        $(this).parents('.dropdown').find('.dropdown-toggle').html($(this).text() + ' <span class="caret"></span>');
        $(this).parents('.dropdown').find('input[name="noise_function"]').val($(this).attr("data-value"));
    });
    $(".dropdown-menu li a").click();
});

var noiseFuncEvent = {};

noiseFuncEvent['none'] = function(){
    var form = document.getElementById('form_noise');
    form.setAttribute('disabled', 'disabled');
    var noise_text = document.getElementById('noise_span');
    noise_text.textContent = 'Noise: ';
}

noiseFuncEvent['uniform'] = function(){
    var form = document.getElementById('form_noise');
    form.removeAttribute('disabled');
    var noise_text = document.getElementById('noise_span');
    noise_text.textContent = 'Noise: ';
}

noiseFuncEvent['gaussian'] = function(){
    var form = document.getElementById('form_noise');
    form.removeAttribute('disabled');
    var noise_text = document.getElementById('noise_span');
    noise_text.textContent = 'Standard variation: ';
}

var tableDownload = function(dataset){
    var content = '';
    for (var k = 0; k < dataset.length; k++){
        content = content + dataset[k].x + ',' + dataset[k].f + '\n';
    }
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(new Blob([content]));
    link.download = "dataset.csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
