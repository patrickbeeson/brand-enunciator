(function ($, Backbone, _, app) {
    var AppRouter = Backbone.Router.extend({
        routes: {
            '': 'home',
            'brand/:slug': 'brand'
        },
        initialize: function (options) {
            this.contentElement = '#content';
            this.current = null;
            Backbone.history.start();
        },
        home: function () {
            var view = new app.views.HomePageView({el: this.contentElement});
            this.render(view);
        },
        brand: function (slug) {
            var view = new app.views.BrandView({
                el: this.contentElement,
                brandSlug: slug
            });
            this.render(view);
        },
        render: function (view) {
            if (this.current) {
                this.current.$el = $();
                this.current.remove();
            }
            this.current = view;
            this.current.render();
        }
    });

    app.router = AppRouter;

})(jQuery, Backbone, _, app);
