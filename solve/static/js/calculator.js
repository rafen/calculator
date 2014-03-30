jQuery(function($, undefined) {
    var domain = 'http://localhost:8000/api/v1/';

    var showHelp = function(term){
        term.echo("Commands:");
        term.echo("save <session__name>");
        term.echo("load <session__name>");
        term.echo("");
        term.echo("Or enter a operation");
    };

    var saveSession = function(name, term){
        var data = JSON.stringify({
            name: name
        });

        $.ajax({
          url: domain+'session/',
          type: 'POST',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          processData: false
        })
            .success(function(data){
                term.echo('Session saved!');
            })
            .fail(function(data){
                term.error(data.statusText);
            });
    };

    var loadSession = function(name, term){
        $.get(domain+"calculator/", {session__name: name, valid:true})
            .success(function( data ) {
                var items = [];
                $.each(data.objects, function(key, value){
                    term.echo(value.equation);
                    term.echo('= '+value.result);
                });
            })
            .fail(function( data ) {
                term.error(data.statusText);
            });
    };


    var solve = function(command, term){
        var data = JSON.stringify({
            equation: command,
            session: null
        });

        $.ajax({
          url: domain+'calculator/',
          type: 'POST',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          processData: false
        })
            .success(function(data){
                if(data.valid){
                    term.echo(data.result);
                }else{
                    term.error('Invalid Syntax');
                    //term.error('Error: '+data.result);
                }
            })
            .fail(function(data){
                term.error(data.statusText);
            });
    };

    var runCommand = function(command, term){
        if(command === 'help'){
            showHelp(term);
        }else if(command.match("^save (.+)")){
            var name = command.match("^save (.+)")[1];
            saveSession(name, term);
        }else if(command.match("^load (.+)")){
            var name = command.match("^load (.+)")[1];
            loadSession(name, term);
        }else{
            solve(command, term);
        }
    };


    $('#term').terminal(function(command, term) {
        if (command !== '') {
            try {
                runCommand(command, term);
            } catch(e) {
                term.error(new String(e));
            }
        } else {
           term.echo('');
        }
    }, {
        greetings: 'Enter commands or equations to solve (type help for more options)',
        name: 'solve',
        height: 200,
        prompt: 'calculator> '});
});