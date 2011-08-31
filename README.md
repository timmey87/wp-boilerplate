A shell of the Washington Post website. Built on a modified version of
the HTML5 boilerplate by Paul Irish, with Compass/SASS and CoffeeScript
support.

### Header

The `#header-v3-external` element can be configured by adding an HTML5
dataset property called `data-config` with GET-style parameters as a
value. For example:

    <div id="header-v3-external" data-config="section=postlive"></div>

#### Possible configuration options

`section`
: String
`subsection`
: String
`weather`
: ?
`subnav`
: Boolean
`hotTopics`
: Boolean
`search`
: Boolean
`utilityLinks`
: Boolean
`userTools`
: Boolean
`adMenu`
: Boolean
`adTiffanyTile`
: Boolean
