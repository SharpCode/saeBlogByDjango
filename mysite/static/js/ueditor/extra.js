window.onload=function(){
	var body=document.getElementById('id_body');
	if(!body)return;
	body.style.width='100%';
	body.style.height='400px';
	body.attributes['type']='text/plain';
	UE.getEditor('id_body');
};
