(function ($, Backbone, _, app) {

    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function () {
            this.template = _.template($(this.templateName).html());
        },
        render: function () {
            var context = this.getContext(),
                html = this.template(context);
            this.$el.html(html);
        },
        getContext: function () {
            return {};
        }
    });

    var HomePageView = TemplateView.extend({
        templateName: '#home-template',
        initialize: function (options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments);
            app.collections.ready.done(function () {
                app.brands.fetch({success: $.proxy(self.render, self)});
            });
        },
        getContext: function () {
            return {brands: app.brands || null};
        }
    });

    var BrandView = TemplateView.extend({
        templateName: '#brand-template',
        initialize: function (options) {
            var self = this;
            TemplateView.prototype.initialize.apply(this, arguments);
            this.brandSlug = options.brandSlug;
            this.brand = null;
            app.collections.ready.done(function () {
                self.brand = app.brands.push({slug: self.brandSlug});
                self.brand.fetch({
                    success: function () {
                        self.render();
                    }
                });
            });
        },
        getContext: function () {
            return {brand: this.brand};
        }
    });

    app.views.Brandview = BrandView;
    app.views.HomePageView = HomePageView;

})(jQuery, Backbone, _, app);
