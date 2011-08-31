A shell of the Washington Post website. Built on a modified version of
the HTML5 boilerplate by Paul Irish, with Compass/SASS and CoffeeScript
support.

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
