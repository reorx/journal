(function() {
    var Commit = Backbone.Model.extend({
    });

    var Settings = Backbone.Model.extend({
    });

    var CommitView = Backbone.View.extend({
    });

    var CommitListView = Backbone.View.extend({
    });

    var SettingsView = Backbone.View.extend({
        events: {
        },

        show: function() {
            this.el.show(1000);
        },

        hide: function() {
            this.el.hide(1000);
        }
    });

    var settingsView = new SettingsView({el: $('.settings')});

    var EditorView = Backbone.View.extend({
    });

    var NavView = Backbone.View.extend({
        activeButton: function(name) {
            this.$('a').removeClass('active');
            this.$(name).addClass('active');
        }
    });

    navView = new NavView({el: $('.nav')});


    var Router = Backbone.Router.extend({
        routes: {
            'today': 'today',
            'oneday': 'oneday',
            'settings': 'settings'
        },

        today: function() {
        },

        oneday: function() {
        },

        settings: function() {
            console.log('settings');
            navView.activeButton('settings');
            settingsView.$el.show();
        }
    })

    router = new Router();

    Backbone.history.start({pushState: true});

    $(document).on('click', 'a:not([data-bypass])', function (e) {

        var href = $(this).attr('href');
        var protocol = this.protocol + '//';

        if (href.slice(protocol.length) !== protocol) {
            e.preventDefault();
            router.navigate(href, true);
        }
    });

})();
