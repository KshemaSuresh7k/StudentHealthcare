from  django  import forms
from .models import crud

class AddFile(forms.ModelForm):
    class Meta:
        model=crud
        fields=('file','image','brochure')
        widgets={
            'file':forms.FileInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'brochure':forms.FileInput(attrs={'class':'form-control'}),
        }    
    

