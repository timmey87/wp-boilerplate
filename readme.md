A shell of the [Washington Post website](http://www.washingtonpost.com). Built on a modified version of
the HTML5 boilerplate by Paul Irish, with Compass/SASS and CoffeeScript
support.

If you'd like to use the HTML5 boilerplate with Compass/SASS and 
CoffeeScript, but without the WaPo header and footer, see [this fork](https://github.com/bcurry/html5-boilerplate).

The `develop.py` script is provided to help consolidate compiling SASS, CoffeeScript,
 and start a simple HTTP server with Python. Run it just by

    python develop.py

Use the following command if you just want to use a simple HTTP server to serve
the files from the current directory.

    python -m SimpleHTTPServer

Then go to [http://localhost:8000/](http://localhost:8000/) to see the server.

### Header

The `#header-v3-external` element can be configured by adding an HTML5
dataset property called `data-config` with GET-style parameters as a
value. For example:

    <div id="header-v3-external" data-config="section=postlive"></div>

#### Possible configuration options

* `section`: String
* `subsection`: String
* `weather`: ?
* `subnav`: Boolean
* `hotTopics`: Boolean
* `search`: Boolean
* `utilityLinks`: Boolean
* `userTools`: Boolean
* `adMenu`: Boolean
* `adTiffanyTile`: Boolean

### Footer

The `#footer-v3-external` element can be configured by adding an HTML5
dataset property called `data-config` with GET-style parameters as a
value. For example:

    <div id="footer-v3-external" data-config="section=postlive"></div>

### General Style Guidelines

* Use double-quotes for HTML, single-quotes for JS. This is to
  reference/create HTML within JS more cleanly (`$('<div id="hello"></div>')`)
* For consistency, don't add trailing slashes for self-closing tags 
  (`img`, `link`, `meta`, etc.).
* Use protocol-relative links (`//goo.gl` instead of `http://goo.gl`).
  This prevents alert messages when mixing HTTP/HTTPS content. (Note:
  this will cause problems when referencing assets while
  testing on a local machine, since it will try to use the `file://`
  protocol. It's recommended to test on a WAMP/MAMP stack.
* Use two spaces for indentation instead of tabs. Some editors treat
  tabs differently, and space-indented files will always look the same.
