$(document).ready(function() {
            // $.getJSON('image_dantri.json', function(data){
            //     console.log(data)
            //     var img = '';
            //     $.each(data.img, function(key, value){
            //         img += '<img src="'+value.source+'" style="width:400px;height:300px;" class="center"></br>';
            //         img += '<h2 style="text-align:center; font-size:200%">'+value.caption+'<h2></br>';
            //     });
            //     $(img).appendTo("#imgdt");
            // });
            // $.getJSON('image_dantri.json', function(data)
            //         {
            //             for(i=0; i < 20; i++)
            //             {
            //                 $("#imgdt").append("<img src="+data.img[i].source+" >" + "\n" + data.img[i].caption + "</br>" + "\n\n");
            //                 $("#imgdt").append("\n");
            //             }
            //         });
            
            $.getJSON('image_tuoitre.json', function(data){
                {
                    img1 += '<img src="'+data.img[1].source+'" style="width:400px;height:300px;" class="center"></br>';
                    img1 += '<h2 style="text-align:center; font-size:200%">'+data.img[1].caption+'<h2></br>';
                }
                $(img1).appendTo("#1");
            });
            $.getJSON('image_tuoitre.json', function(data){
                {
                    ("#2").append("<img src="+data.img[8].source+" >" + "\n" + "</br>" + data.img[8].caption + "\n\n");
                }
            });
            $.getJSON('image_tuoitre.json', function(data){
                console.log(data)
                var img = '';
                $.each(data.img, function(key, value){
                    img += '<img src="'+value.source+'" style="width:400px;height:300px;" class="center"></br>';
                    img += '<h2 style="text-align:center; font-size:200%">'+value.caption+'<h2></br>';
                });
                $(img).appendTo("#imgtt");
            });
            $.getJSON('image_vnexpress.json', function(data){
                console.log(data)
                var img = '';
                $.each(data.img, function(key, value){
                    img += '<img src="'+value.source+'" style="width:400px;height:300px;" class="center"></br>';
                    img += '<h2 style="text-align:center; font-size:200%">'+value.caption+'<h2></br>';
                });
                $(img).appendTo("#imgve");
            });
});
