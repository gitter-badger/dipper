from dipper.models.assoc.Association import Assoc

__author__ = 'nlw'


class DispositionAssoc(Assoc):
    """
    A specific Association model for Heritability annotations.
    These are to be used between diseases and a heritability disposition.
    """

    def __init__(self, definedby, entity_id, heritability_id):
        super().__init__(definedby)

        self.set_subject(entity_id)
        self.set_object(heritability_id)
        # default to has_disposition
        self.set_relationship(self.object_properties['has_disposition'])

        return
