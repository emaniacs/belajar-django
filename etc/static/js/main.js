$.fn.hargaIndonesia = function() {
    return this.each(function() {
        var self = $(this),
            html = self.html()
        ;
        self.html(html + ',--');
    })
}
