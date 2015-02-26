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
        events: {
            // 'click video': 'videoControls',
            'click video': 'updateCounter',
            'click .video video': 'playVideo',
            'click .sound': 'muteVideo',
            'click .js-open-card': 'openCard'
        },
        initialize: function (options) {
            var self = this;

            TemplateView.prototype.initialize.apply(this, arguments);
            app.collections.ready.done(function () {
                app.brands.fetch({success: $.proxy(self.render, self)});
            });
        },
        getContext: function () {
            return {brands: app.brands || null};
        },
        updateCounter: function (e) {
            var id = $(e.currentTarget).data('id');
            var item = self.app.brands.get(id);
            var views = item.get('video_views');
            var video = $(e.currentTarget);
            // Only update the counter if the video is in play state
            if (video.prop('paused')) {
                item.save({video_views: views + 1}, {patch: true});
                this.render();
            }
        },
        playVideo: function (e) {
            var id = $(e.currentTarget).data('id');
            var video = $('#' + id);
            if (video.prop('paused')) {
                video[0].play();
            } else {
              video.get(0).pause();
            }
        },
        muteVideo: function (e) {
            e.preventDefault();
            var video = $(e.currentTarget).parent().find('video');
            video.prop('muted', !video.prop('muted'));
            $(e.currentTarget).toggleClass('is-muted');
        },
        openCard: function (e) {
            e.preventDefault();
            $(e.currentTarget).toggleClass('is-open');
            $(e.currentTarget).closest('.card-container').toggleClass('is-open');
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
