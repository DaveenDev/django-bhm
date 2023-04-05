function formatMoney(amount) {
  return (amount).toFixed(2)
                .replace(/\d(?=(\d{3})+\.)/g, '$&,'); 
}


function showNotification(message, title=''){
    $.notify({
        title: title,
        message: message
     },
     {
        type:'primary',
        allow_dismiss:false,
        newest_on_top:false ,
        mouse_over:false,
        showProgressbar:false,
        spacing:10,
        timer:2000,
        placement:{
          from:'top',
          align:'center'
        },
        offset:{
          x:30,
          y:30
        },
        delay:1000 ,
        z_index:10000,
        animate:{
          enter:'animated bounce',
          exit:'animated bounce'
      }
    });

}