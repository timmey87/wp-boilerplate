site = 
  common:
    init: ->
      # Application-wide code
  main:
    init: ->
      # Controller-wide code
    home: ->
      # Action-specific code

util =
  exec: (controller, action) ->
    action ?= 'init'
    site[controller][action]?() if site[controller]
  init: ->
    body = document.body
    controller = body.getAttribute 'data-controller'
    action = body.getAttribute 'data-action'
    util.exec 'common'
    util.exec controller
    util.exec controller, action

$(document).ready util.init
