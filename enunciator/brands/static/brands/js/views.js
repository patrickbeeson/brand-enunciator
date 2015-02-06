(function ($, Backbone, _, app) {
    var HomePageView = Backbone.View.extend({
        templateName: '#home-template',
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

    app.views.HomePageView = HomePageView;

})(jQuery, Backbone, _, app);
