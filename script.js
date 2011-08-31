(function() {
  var site, util;
  site = {
    common: {
      init: function() {}
    },
    main: {
      init: function() {},
      home: function() {}
    }
  };
  util = {
    exec: function(controller, action) {
      var _base;
      if (action == null) {
        action = 'init';
      }
      if (site[controller]) {
        return typeof (_base = site[controller])[action] === "function" ? _base[action]() : void 0;
      }
    },
    init: function() {
      var action, body, controller;
      body = document.body;
      controller = body.getAttribute('data-controller');
      action = body.getAttribute('data-action');
      util.exec('common');
      util.exec(controller);
      return util.exec(controller, action);
    }
  };
  $(document).ready(util.init);
}).call(this);
