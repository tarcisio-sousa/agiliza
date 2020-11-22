from django.forms import ModelForm
from core.base.models import Proposta

class PropostaForm(ModelForm):
	class Meta:
		model = Proposta
		fields = '__all__'

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['prefeitura'].widget.attrs.update({'class': 'form-control custom-select'})
	    self.fields['lei_complementar'].widget.attrs.update({'class': 'form-control'})
	    self.fields['data_lei'].widget.attrs.update({'class': 'form-control'})
	    self.fields['valor_contrapartida'].widget.attrs.update({'class': 'form-control'})
	    self.fields['objeto'].widget.attrs.update({'class': 'form-control'})
	    self.fields['numero_proposta'].widget.attrs.update({'class': 'form-control'})