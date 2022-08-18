# Common stuff
#######

techdict = {
        'python':{'icon':'static/icons/python.svg', 'name':'Python', 'link':'https://www.python.org'},
        'javascript':{'icon':'static/icons/javascript.svg', 'name':'JavaScript (JS)', 'link':'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        'sql':{'icon':'static/icons/sql.svg','name':'PostgreSQL', 'link':'https://www.postgresql.org'},
        'html':{'icon':'static/icons/html.svg','name':'HTML', 'link':'https://developer.mozilla.org/en-US/docs/Web/HTML'},
        'css':{'icon':'static/icons/css.svg', 'name':'CSS', 'link':'https://developer.mozilla.org/en-US/docs/Web/CSS'},
        'flask':{'icon':'static/icons/flask.svg', 'name':'Flask', 'link':'https://flask.palletsprojects.com/en/2.2.x/'},
        'django':{'icon':'static/icons/django.svg', 'name':'Django', 'link':'https://www.djangoproject.com'},
        'github':{'icon':'static/icons/github.png', 'name':'GitHub', 'link':'https://github.com'},
        'heroku':{'icon':'static/icons/heroku.png', 'name':'Heroku', 'link':'https://www.heroku.com/'},
        'wordpress':{'icon':'static/icons/wordpress.svg', 'name':'WordPress', 'link':'https://wordpress.com'},
        'mongodb':{'icon':'static/icons/mongodb.svg', 'name':'MongoDB', 'link':'https://www.mongodb.com'},
        'bulma':{'icon':'static/icons/bulma.png', 'name':'Bulma', 'link':'https://bulma.io'},
        'bootstrap':{'icon':'static/icons/bootstrap.png', 'name':'Bootstrap', 'link':'https://getbootstrap.com'},
    }

footer = {
    'techlist':['python','flask', 'bulma'],
    'techdict': techdict,
    'deployed':'heroku',
}


# pages
#######
projects = {
    'projects':{
        'stockmarket':{
            'title':'The Stock Market',
            'images':'static/stockmarket.png',
            'words':['blah blah blah','blah blah blah', 'blah blah blah'],
            'techlist':['python','flask','bootstrap'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com'
        },
        'project2':{
            'title':'Project Two',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['javascript','django','bulma'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project3':{
            'title':'Project Three',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['github','heroku','sql'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project4':{
            'title':'Project Four',
            'images':'static/stockmarket.png',
            'words':['blah blah blah','blah blah blah', 'blah blah blah'],
            'techlist':['python','flask','bootstrap'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com'
        },
        'project5':{
            'title':'Project Two',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['javascript','django','bulma'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project6':{
            'title':'Project Three',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['github','heroku','sql'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project7':{
            'title':'The Stock Market',
            'images':'static/stockmarket.png',
            'words':['blah blah blah','blah blah blah', 'blah blah blah'],
            'techlist':['python','flask','bootstrap'],
            'techdict': techdict,
            'link':'https://lit-eyrie-84189.herokuapp.com'
        },
        'project8':{
            'title':'Project Two',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['javascript','django','bulma'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
        'project9':{
            'title':'Project Three',
            'images':'static/stockmarket.png',
            'words':['blah blah blah', 'blah blah blah', 'blah blah blah'],
            'techlist':['github','heroku','sql'],
            'techdict': techdict,
            'link':'https://www.google.com'
        },
    },
    'footer':footer
}



home = {
    'title': 'Welcome',
    'quote': 'something neat and clever',
    'words': 'blah, blah, blah...for now...this may need to be a list or dict',
    'icons': {
        'python':{'icon':'static/icons/python.svg', 'name':'Python', 'link':'https://www.python.org'},
        'javascript':{'icon':'static/icons/javascript.svg', 'name':'JavaScript (JS)', 'link':'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        'sql':{'icon':'static/icons/sql.svg','name':'PostgreSQL', 'link':'https://www.postgresql.org'},
        'html':{'icon':'static/icons/html.svg','name':'HTML', 'link':'https://developer.mozilla.org/en-US/docs/Web/HTML'},
        'css':{'icon':'static/icons/css.svg', 'name':'CSS', 'link':'https://developer.mozilla.org/en-US/docs/Web/CSS'},
        'flask':{'icon':'static/icons/flask.svg', 'name':'Flask', 'link':'https://flask.palletsprojects.com/en/2.2.x/'},
        'django':{'icon':'static/icons/django.svg', 'name':'Django', 'link':'https://www.djangoproject.com'},
        'github':{'icon':'static/icons/github.png', 'name':'GitHub', 'link':'https://github.com'},
        'heroku':{'icon':'static/icons/heroku.png', 'name':'Heroku', 'link':'https://www.heroku.com/'},
        'wordpress':{'icon':'static/icons/wordpress.svg', 'name':'WordPress', 'link':'https://wordpress.com'},
        'mongodb':{'icon':'static/icons/mongodb.svg', 'name':'MongoDB', 'link':'https://www.mongodb.com'},
        'bulma':{'icon':'static/icons/bulma.png', 'name':'Bulma', 'link':'https://bulma.io'},
        'bootstrap':{'icon':'static/icons/bootstrap.png', 'name':'Bootstrap', 'link':'https://getbootstrap.com'},
    },
    'university':{
        'uco':{'images':'static/uco.png', 'title':'University of Colorado', 'words':['University of Colorado, yay!', 'more and more', '...and a bit more'], 'link':'https://colorado.edu'},
        'und':{'images':'static/und.png', 'title':'University of Notre Dame', 'words':['University of Notre Date, yay!', 'more and more', '...and a bit more'], 'link':'https://www.nd.edu'},
        'uca':{'images':'static/uca.png', 'title':'University of California', 'words':['University of California, yay!', 'more and more', '...and a bit more'], 'link':'https://www.berkeley.edu'}
    },
    'footer': footer
}



fun = {
    'locs' : ['maroonbells', 'stream', 'megatron','garden', 'starbase', 'carmel'],
    'images' : {
        'garden':'static/garden.jpeg',
        'maroonbells':'static/maroonbells.jpeg',
        'starbase':'static/starbase.jpeg',
        'megatron':'static/megatron.jpeg',
        'carmel':'static/carmel.jpeg',
        'stream':'static/stream.jpeg',
    },
    'words' : {
        'garden':["rocket garden blah", "rocket garden blah blah", "rocket garden blah blah blah"],
        'maroonbells':["maroonbells blah", "maroonbells blah blah", "maroonbells blah blah blah"],
        'starbase':["starbase  blah", "starbase  blah blah", "starbase  blah blah blah"],
        'megatron':["megatron blah", "megatron blah blah", "megatron blah blah blah"],
        'carmel':["carmel blah", "blah", "blah"],
        'stream':["stream blah", "blah", "blah"],
    },
    'links' : {
        'garden':'https://goo.gl/maps/ao5J71RrhYNk6t8r7',
        'maroonbells':"https://goo.gl/maps/KV2tuxrd3RKb1wRv6",
        'starbase':'https://goo.gl/maps/ao5J71RrhYNk6t8r7',
        'megatron': "https://goo.gl/maps/kdun97NejvLk1uvg6",
        'carmel':'https://goo.gl/maps/VqZXdhyBNZxTizmw9',
        'stream':'https://goo.gl/maps/nB7yJQzNaukAa9ZN6'
    },
    'titles' : {
        'garden':'Rocket Garden at Starbase, TX',
        'maroonbells':'Maroon Bells near Aspen, CO',
        'starbase':'"The Sign" at Starbase, TX',
        'megatron':'Starbase Launch Complex and "Megatron" near Boca Chica Beach, TX',
        'carmel':'Pebble Beach near Carmel, CA',
        'stream':'Pfiefer Big Sur State Park south of Carmel, CA',
    },
    'footer':footer,
}

contact = {
    'k': ['linkedin', 'email', 'github', 'twitter'],
    'images': {
        'linkedin':'static/icons/linkedin.png',
        'email':'static/icons/email.png',
        'twitter':'static/icons/twitter.png',
        'github':'static/icons/github.png',
    },
    'links': {
        'linkedin':'https://www.linkedin.com/in/justinhanson1/',
        'email':'hansonjw@gmail.com',
        'twitter':'https://twitter.com/hansonjw',
        'github':'https://github.com/hansonjw',
    },
    'href': {
        'linkedin':'https://www.linkedin.com/in/justinhanson1/',
        'email':'mailto:hansonjw@gmail.com',
        'twitter':'https://twitter.com/hansonjw',
        'github':'https://github.com/hansonjw',
    },
    'footer':footer,
}