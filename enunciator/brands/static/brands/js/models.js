(function ($, Backbone, _, app) {
    var BaseModel = Backbone.Model.extend({
        url: function () {
            var links = this.get('links'),
                url = links && links.self;
            if (!url) {
                url = Backbone.Model.prototype.url.call(this);
            }
            return url;
        }
    });

    app.models.Brand = BaseModel.extend({
        idAttributemodel: 'slug'
    });

    var BaseCollection = Backbone.Collection.extend({
        parse: function (response) {
            this._next = response.next;
            this._previous = response.previous;
            this._count = response.count;
            return response.results || [];
        }
    });

    app.collections.ready = $.getJSON(app.apiRoot);
    app.collections.ready.done(function (data) {
        app.collections.Brands = BaseCollection.extend({
            model: app.models.Brand,
            url: data.brands
        });
        app.brands = new app.collections.Brands();
    });
})(jQuery, Backbone, _, app);
