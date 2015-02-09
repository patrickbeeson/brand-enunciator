(function ($, Backbone, _, app) {

    var TemplateView = Backbone.View.extend({
        templateName: '',
        initialize: function () {
            this.template = _.template($(this.templateName).html());
        },
        render: function () {
            var context = this.getContext(), html = this.template(context);
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
            this.brandId = options.brandId;
            this.brand = null;
            app.collections.ready.done(function () {
                app.brands.getOrFetch(self.brandId).done(function (brand) {
                    self.brand = brand;
                    self.render();
                }).fail(function (brand) {
                    self.brand = brand;
                    self.brand.invalid = true;
                    self.render();
                });
            });
        },
        getContext: function () {
            return {brand: this.brand};
        }
    });

    app.views.HomePageView = HomePageView;
    app.views.BrandView = BrandView;

})(jQuery, Backbone, _, app);
