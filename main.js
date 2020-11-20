 $(document).ready(function() {
            $.getJSON('image_dantri.json', function(data){
                console.log(data)
                var img = '';
                $.each(data.img, function(key, value){
                    img += '<tr>';
                    img += '<td>'+value.caption+'</td>';
                    img += '<td><img src="'+value.source+'"></td>';
                    img += '</tr>';
                });
                $(img).appendTo("#news tbody");
            });
            $.getJSON('image_tuoitre.json', function(data){
                console.log(data)
                var img = '';
                $.each(data.img, function(key, value){
                    img += '<tr>';
                    img += '<td>'+value.caption+'</td>';
                    img += '<td><img src="'+value.source+'"></td>';
                    img += '</tr>';
                });
                $(img).appendTo("#news tbody");
            });
            $.getJSON('image_vnexpress.json', function(data){
                console.log(data)
                var img = '';
                $.each(data.img, function(key, value){
                    img += '<tr>';
                    img += '<td>'+value.caption+'</td>';
                    img += '<td><img src="'+value.source+'"></td>';
                    img += '</tr>';
                });
                $(img).appendTo("#news tbody");
            });
        });
