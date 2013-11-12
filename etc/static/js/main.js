$.fn.hargaIndonesia = function() {
    return this.each(function() {
        var self = $(this),
            html = self.html(),
            arr = html.split(''),
            rev = arr.reverse(),
            ret = []
        ;
        
        $.each(rev, function(index, obj) {
            if (index != 0 && index % 3 == 0) {
                ret.push('.');
            }
            
            ret.push(obj);
        })
        
        self.html(ret.reverse().join(''));
    })
}
