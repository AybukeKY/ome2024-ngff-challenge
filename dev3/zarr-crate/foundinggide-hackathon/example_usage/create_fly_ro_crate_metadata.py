import json
from zarr_crate.zarr_extension import ZarrCrate
from zarr_crate.rembi_extension import (Biosample, Specimen, ImageAcquistion, 
                                        IntrinsicVariable, ExtrinsicVariable, Gene, ChemicalSubstance) 


if __name__ == "__main__":
    crate = ZarrCrate()

    zarr_root = crate.add_dataset(
        "./",
        properties={
            "name": "Test Light microscopy photo of a fly",
            "description": "Light microscopy photo of a fruit fly.",
            "license": "https://creativecommons.org/licenses/by/4.0/",
        },
    )
    gene = crate.add(
        Gene(crate, properties={"@id": "ENSG00000010404",
        "@type": "Gene",
        "identifier": "ENSG00000010404",
        "taxonomicRange": "Ensembl:ENSG00000010404"})
    )
    
    intvariable = crate.add(IntrinsicVariable(crate, gene))

    chemsubstance1 = crate.add(
        ChemicalSubstance(crate, properties={
        "@type": ["ChemicalSubstance", "Compound"],
        "identifier": "CHEBI:17790",
        "name": "methanol"})
    )
    chemsubstance2 = crate.add(
        ChemicalSubstance(crate, properties={
        "@type": ["ChemicalSubstance", "Reagent"],
        "identifier": "CHEBI:51231",
        "name": "DAPI"})
    )

    extvariable = crate.add(ExtrinsicVariable(crate, chemsubstance1, chemsubstance2))

    biosample = crate.add(
        Biosample(
            crate, intvariable, extvariable, properties={"organism_classification": {"@id": "NCBI:txid7227"}}
        )
    )
    specimen = crate.add(Specimen(crate, biosample))
    image_acquisition = crate.add(
        ImageAcquistion(
            crate, specimen, properties={"fbbi_id": {"@id": "obo:FBbi_00000243"}}
        )
    )
    zarr_root["resultOf"] = image_acquisition

    metadata_dict = crate.metadata.generate()

    with open("ro-crate-metadata.json", "w") as f:
        f.write(json.dumps(metadata_dict, indent=2))
