$(document).ready(function(){
	var ip = "localhost"
	var ws = new WebSocket('ws://'+ ip +':8000/soc');
		ws.onmessage = function(event){
			// var conversation = document.getElementById('message');
			box = $('#message');
			var data = eval('(' + event.data + ')');
			({
				'sys':function() {
					addMessage(box,'<div class="center sysinfo">' + data['message'] + '</div>' )
				},
				'user':function() {
					addMessage(box,'<div class="textbox fromother">' +
						data ['message']['content'] +
						'</div>')
					// $('#message').append('<div class="textbox fromother">' +
					// 	data ['message'] +
					// 	'</div>')
				},
				'self': function() {
					addMessage(box,'<div class="textbox fromself">' +
						data ['message']['content'] +
						'</div>')
					// $('#message').append('<div class="textbox fromself">' +
					// 	data ['message'] +
					// 	'</div>')
				},
				'term': function() {
					// console.log(data['message'][0])
					console.log(data['message']);

					nodeparentlabel = data['message']['parent'];
					var parentnode = null;
					if (nodeparentlabel != ''){
						$.each(graph.nodes, function(index, val) {
							if (val['data']['label'] == nodeparentlabel){
								parentnode = val;
							}
						});
					}

					$.each(data['message']['termlist'],function(key,value){
						console.log(parentnode);
						$('#foo').trigger("click",[value, parentnode]);
					})
					

					
				},
			}[data['type']])();

			
			$("#messagebox").animate({ scrollTop: $('#messagebox')[0].scrollHeight}, 1000);
	};

	function addMessage(div,message) {
		div.append('<div class="row"><div class="col-md-12">' + message + '</div></div>');
		// div.append(message);
		// div.append('</row>')
	}

	function send() {
		message = {
			'content': $("#chat").val(),
			'parent': selectnode
		}
		// ws.send(document.getElementById('chat').value);
		ws.send(JSON.stringify(message));
		document.getElementById('chat').value = '';
		// $("#foo").trigger("click");
	}
        
      
    $("#sendbutton").click(function() {
        	console.log("click send");
        	send();
    });

    var connectstatus = false;
	$("#connectbutton").click(function() {
		if (connectstatus) {
			$("#connectbutton").removeClass("active");
			$("#connectbutton").text("Connect");
			console.log("Connect");
			connectstatus = false;
			lastNodeSelected = null;
		} else {
			$("#connectbutton").addClass("active");
			$("#connectbutton").text("Connecting");
			console.log("Connecting");
			connectstatus = true;
		}
	});

	$("#deletenode").click(function() {
		console.log("delete");
		$("#selectnode").val('');
		selectnode = '';	
	});

	$(document).keypress(function(e) {  
	// 回车键事件  
		if(e.which == 13) {  
			send(); 
		}  
	}); 








	//====================================//
	$("#chat").focus();

	var graph = new Springy.Graph();
	// var topicnode = graph.newNode({
	// 	label: "Topic"
	// })
	// graph.addNodes('Topic');


	colorList = [
		'#00A0B0',
		'#6A4A3C',
		'#CC333F',
		'#EB6841',
		'#7DBE3C',
		'#BE7D3C',
		'#6A4A3C'
		]

	var canvas = document.getElementById("viewport");
	console.log($("#termMap").width() + ":" + $("#termMap").height())
	canvas.width = $("#termMap").width();
	canvas.height = $("#termMap").height();

	var lastNodeSelected = null;

	var springy = $("#viewport").springy({
		graph:graph,
		nodeSelected: function(node){
			if (connectstatus)
			{
				if (lastNodeSelected != null && lastNodeSelected != node){
									newEdgeRequest(lastNodeSelected, node);
									lastNodeSelected = null;
							} else {
									lastNodeSelected = node;
							}
						
						console.log("select");}
			// console.log(JSON.stringify(node.data));
		}
	});
	var selectnode = '';
	$("#foo").on("click", function(event, term, parentnode){
		console.log(parentnode);
		var newnode = graph.newNode({
			label: term,
			ondoubleclick: function() {
				$("#selectnode").val(term);
				selectnode = term;

				
				console.log("Double click");
			}
		});

		if (parentnode != null){
			newEdgeRe(parentnode,newnode);
		}
		// console.log(graph);
		// graph.addNodes(term);

		// graph.addNodes(newnode);
		// graph.addEdges(['Topic', newnode, {color: colorList[getRandomInt(0,6)]}])
		// graph.newEdge(topicnode,newnode,{color: colorList[getRandomInt(0,6)]});
		// newEdgeWithColor(topicnode, newnode);
	})

	function getRandomInt(min, max) {
		return Math.floor(Math.random() * (max - min + 1) + min);
	}

	function newEdgeRequest(node1, node2){
		message = {
			'child': node1['data']['label'],
			'parent': node2['data']['label']
		}
		// ws.send(document.getElementById('chat').value);
		ws.send(JSON.stringify(message));
	}

	function newEdgeWithColor(node1, node2){
		graph.newEdge(node1,node2,{color: colorList[getRandomInt(0,6)]});
	}

})

