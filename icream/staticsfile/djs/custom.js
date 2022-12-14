
function deleteproduct(productid){
    swal({
        title: "Are you sure?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          
          $.ajax({
            url : 'remove',
            type : 'GET',
            data : {
                'productid' : productid
            },
            success : function(data){
                location.href = ''
                console.log(data.value)
            }
          })

        } else {
          console.log(false)
        }
      });
}




function blockuser(productid){
    swal({
        title: "Are you sure?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          
          $.ajax({
            url : 'block',
            type : 'GET',
            data : {
                'productid' : productid
            },
            success : function(data){
                location.href = ''
                console.log(data.value)
            }
          })

        } else {
          console.log(false)
        }
      });
}
