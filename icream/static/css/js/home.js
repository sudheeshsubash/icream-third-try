
function addtocart(pid){
  console.log(pid)
  $.ajax({
      url : 'addcart',
      type : 'GET',
      data : {
          'pid' : pid
      },
      success : function(data){
        if(data.value == 1){
          swal({
              title: "Already Added",
              icon: "info",
            })
      }else if(data.value == 0){
          swal({
              title: "Add To Cart",
              icon: "success",
            })
      }
      }
  })
}

 


function removewishlist(productid){
    swal({
        title: "Are you sure?",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          swal("Remove ", {
            icon: "success",
          });
          
          $.ajax({
            url : 'remove',
            type : 'GET',
            data : {
                'productid' : productid
            },
            success : function(data){
                location.href = ''
            }
          })

        } else {
          console.log(false)
        }
      });
}

