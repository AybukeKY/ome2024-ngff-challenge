from rocrate.model.contextentity import ContextEntity


class Biosample(ContextEntity):
    def __init__(self, crate, intvariable, extvariable, identifier=None, properties=None):
        biosample_type_path = "biosample"
        if properties:
            biosample_properties = {}
            biosample_properties.update(properties)
            if "@type" in properties.keys():
                biosample_types = biosample_properties["@type"]
                if biosample_type_path not in biosample_types:
                    try:
                        biosample_types.append(biosample_type_path)
                    except:
                        biosample_types = [biosample_types]
                        biosample_types.append(biosample_type_path)
                    biosample_properties["@type"] = biosample_types
            else:
                biosample_properties.update({"@type": biosample_type_path})
        else:
            biosample_properties = {"@type": biosample_type_path}

        super().__init__(crate, identifier, biosample_properties)
        self["intrinsic_variable"] = intvariable
        self["extrinsic_variable"] = extvariable

class IntrinsicVariable(ContextEntity):
    def __init__(self, crate, gene, identifier=None, properties=None):
        intvariable_type_path = "intrinsic_variable"
        if properties:
            intvariable_properties = {}
            intvariable_properties.update(properties)
            if "@type" in properties.keys():
                intvariable_types = intvariable_properties["@type"]
                if intvariable_type_path not in intvariable_types:
                    try:
                        intvariable_types.append(intvariable_type_path)
                    except:
                        intvariable_types = [intvariable_types]
                        intvariable_types.append(intvariable_type_path)
                    intvariable_properties["@type"] = intvariable_types
            else:
                intvariable_properties.update({"@type": intvariable_type_path})
        else:
            intvariable_properties = {"@type": intvariable_type_path}

        super().__init__(crate, identifier, intvariable_properties)
        self["Gene"] = gene

class ExtrinsicVariable(ContextEntity):
    def __init__(self, crate, chemsubstance, identifier=None, properties=None):
        extvariable_type_path = "extrinsic_variable"
        if properties:
            extvariable_properties = {}
            extvariable_properties.update(properties)
            if "@type" in properties.keys():
                extvariable_types = extvariable_properties["@type"]
                if extvariable_type_path not in extvariable_types:
                    try:
                        extvariable_types.append(extvariable_type_path)
                    except:
                        extvariable_types = [extvariable_types]
                        extvariable_types.append(extvariable_type_path)
                    extvariable_properties["@type"] = extvariable_types
            else:
                extvariable_properties.update({"@type": extvariable_type_path})
        else:
            extvariable_properties = {"@type": extvariable_type_path}

        super().__init__(crate, identifier, extvariable_properties)
        self["ChemicalSubstance"] = chemsubstance

class Gene(ContextEntity):
    def __init__(self, crate, identifier=None, properties=None):
        gene_type_path = "Gene"
        if properties:
            gene_properties = {}
            gene_properties.update(properties)
            if "@type" in properties.keys():
                gene_types = gene_properties["@type"]
                if gene_type_path not in gene_types:
                    try:
                        gene_types.append(gene_type_path)
                    except:
                        gene_types = [gene_types]
                        gene_types.append(gene_type_path)
                    gene_properties["@type"] = gene_types
            else:
                gene_properties.update({"@type": gene_type_path})
        else:
            gene_properties = {"@type": gene_type_path}

        super().__init__(crate, identifier, gene_properties)

class ChemicalSubstance(ContextEntity):
    def __init__(self, crate, identifier=None, properties=None):
        chemsubstance_type_path = "ChemicalSubstance"
        if properties:
            chemsubstance_properties = {}
            chemsubstance_properties.update(properties)
            if "@type" in properties.keys():
                chemsubstance_types = chemsubstance_properties["@type"]
                if chemsubstance_type_path not in chemsubstance_types:
                    try:
                        chemsubstance_types.append(chemsubstance_type_path)
                    except:
                        chemsubstance_types = [chemsubstance_types]
                        chemsubstance_types.append(chemsubstance_type_path)
                    chemsubstance_properties["@type"] = chemsubstance_types
            else:
                chemsubstance_properties.update({"@type": chemsubstance_type_path})
        else:
            chemsubstance_properties = {"@type": chemsubstance_type_path}

        super().__init__(crate, identifier, chemsubstance_properties)
class Specimen(ContextEntity):
    def __init__(self, crate, biosample, identifier=None, properties=None):
        specimen_type_path = "specimen"
        if properties:
            specimen_properties = {}
            specimen_properties.update(properties)
            if "@type" in properties.keys():
                specimen_type = specimen_properties["@type"]
                if specimen_type_path not in specimen_type:
                    try:
                        specimen_type.append(specimen_type_path)
                    except:
                        specimen_type = [specimen_type]
                        specimen_type.append(specimen_type_path)
                    specimen_properties["@type"] = specimen_type
            else:
                specimen_properties.update({"@type": specimen_type_path})
        else:
            specimen_properties = {"@type": specimen_type_path}

        super().__init__(crate, identifier, specimen_properties)

        self["biosample"] = biosample


class ImageAcquistion(ContextEntity):
    def __init__(self, crate, specimen, identifier=None, properties=None):
        image_acquisition_type_path = "image_acquisition"
        if properties:
            image_acquisition_properties = {}
            image_acquisition_properties.update(properties)
            if "@type" in properties.keys():
                image_acquisition_type = image_acquisition_properties["@type"]
                if image_acquisition_type_path not in image_acquisition_type:
                    try:
                        image_acquisition_type.append(image_acquisition_type_path)
                    except:
                        image_acquisition_type = [image_acquisition_type]
                        image_acquisition_type.append(image_acquisition_type_path)
                    image_acquisition_properties["@type"] = image_acquisition_type
            else:
                image_acquisition_properties.update(
                    {"@type": image_acquisition_type_path}
                )
        else:
            image_acquisition_properties = {"@type": image_acquisition_type_path}

        super().__init__(crate, identifier, image_acquisition_properties)

        self["specimen"] = specimen
