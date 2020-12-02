$(document).ready(function()
{   
        $.getJSON("./image_dantri.json", function(data)
        {
            var i;
            for(i=0; i<30; ++i)
                {
                    $("#dt" + i).append("<a href='" + data.img[i].news_source + "'><img src ='" + data.img[i].source + "'></a>");
                    $("#dtct" + i).append("<a href='" + data.img[i].news_source + "'>" + data.img[i].caption + "</a>");
                }
        });
        $.getJSON("./image_tuoitre.json", function(data)
        {
            var i;
            for(i=0; i<30; ++i)
                {
                    $("#tt" + i).append("<a href='" + data.img[i].news_source + "'><img src ='" + data.img[i].source + "'></a>");
                    $("#ttct" + i).append("<a href='" + data.img[i].news_source + "'>" + data.img[i].caption + "</a>");
                }
        });
        $.getJSON("./image_vnexpress.json", function(data)
        {
            var i;
            for(i=0; i<30; ++i)
                {
                    $("#ve" + i).append("<a href='" + data.img[i].news_source + "'><img src ='" + data.img[i].source + "'></a>");
                    $("#vect" + i).append("<a href='" + data.img[i].news_source + "'>" + data.img[i].caption + "</a>");
                }
        });
});