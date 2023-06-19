function showNotification(message, title=''){

  $.notify({
    title: title,
    message: message
 },
 {
    type:'primary',
    allow_dismiss:true,
    newest_on_top:false ,
    mouse_over:false,
    showProgressbar:false,
    spacing:10,
    timer:1000,
    placement:{
      from:'bottom',
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

function showErrorNotification(message, title=''){

  $.notify({
    title: title,
    message: message
  },
  {
    type:'warning',
    allow_dismiss:true,
    newest_on_top:false ,
    mouse_over:false,
    showProgressbar:false,
    spacing:10,
    timer:2000,
    placement:{
      from:'bottom',
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

window.showNotification = showNotification
window.showErrorNotification = showErrorNotification