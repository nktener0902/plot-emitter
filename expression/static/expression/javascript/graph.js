function createsvg(dataset){
    dataset = dataset.replace(/&#39;/g, '"');
    dataset_json = JSON.parse(dataset);

    var margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = 600 - (margin.left + margin.right),
        height = 400 - (margin.top + margin.bottom);

    var svg = d3.select('#graph')
        .attr({
            width: width + (margin.left + margin.right),
            height: height + (margin.top + margin.bottom)
        })
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var x_min = Math.min.apply( null, dataset_json.map( function(d){return d.x;}));
    var x_max = Math.max.apply( null, dataset_json.map( function(d){return d.x;}));
    var xScale = d3.scale.linear()
        .domain([x_min, x_max])
        .range([0, width]);
    var f_min = Math.min.apply( null, dataset_json.map( function(d){return d.f;}));
    var f_max = Math.max.apply( null, dataset_json.map( function(d){return d.f;}));
    var yScale = d3.scale.linear()
        .domain([f_min, f_max])
        .range([height, 0]);

    // Data binding
    svg.selectAll('circle')
        .data(dataset_json)
        .enter()
        .append('circle');

    // Drawing
    svg.selectAll('circle')
        .attr({
            cx: function(d){return xScale(parseFloat(d.x))},
            cy: function(d){return yScale(parseFloat(d.f))},
            r: function(d){return 3},
            fill: "red"
        });

    // Text
    svg.selectAll("text")
        .attr({
            'x': function(d){return xScale(d.x);},
            'f': function(d){return yScale(d.y);}
        })
        .attr("font-family", "sans-serif")
        .attr("font-size", "11px")
        .attr("fill", "red")

    // Axis
    var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient("bottom");
    var yAxis = d3.svg.axis()
        .scale(yScale)
        .orient("left");

    svg.append("g")
        .attr("class", "axis")
        .call(yAxis)
        .append("y", -10)
        .attr("f", 20)
        .style("text-anchor", "end");

    svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
}
