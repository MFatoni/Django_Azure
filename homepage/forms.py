from django import forms

class Biodata_Forms(forms.Form):
	error_messages={
		'required' :'Tolong isi input ini',
		'invalid' : 'isi input dengan email'
	}
	attrs_name={
		'class':'form-control mb-2',
		'placeholder':'Nama'
	}
	attrs_email={
		'class':'form-control',
		'placeholder':'Email'
	}
	name = forms.CharField(label='',required=True,widget=forms.TextInput(attrs=attrs_name))
	email = forms.EmailField(label='',required=True,widget=forms.EmailInput(attrs=attrs_email))

