# UPGMA Starter Code

## Data

The `Data/` folder contains eight biological datasets, each in its own subfolder. Every subfolder includes a `.mtx` file (the distance matrix you will pass to your UPGMA implementation) and, where available, a `.fasta` file containing the original protein or nucleotide sequences the distances were computed from. Distances are Levenshtein (edit) distances between sequences unless noted otherwise.

---

### HBA1 — Hemoglobin Subunit Alpha
Protein sequences for hemoglobin subunit alpha (HBA1) from 108 animals, downloaded from UniProt. A classic molecular clock protein used to study evolutionary relationships across vertebrates.

### Cytochrome-C — Somatic Cytochrome C
Cytochrome c sequences (~104–112 amino acids) from 16 diverse eukaryotes. Because cytochrome c evolves slowly under strong functional constraint, it obeys a molecular clock reasonably well, making it a canonical target for UPGMA. The resulting tree broadly recapitulates the accepted phylogeny of eukaryotes.

### Cetaceans — Cetacean Phylogeny
Mitochondrial cytochrome b protein sequences for 12 mammalian species. This dataset illustrates one of the most surprising results in molecular phylogenetics: whales and dolphins evolved from within the even-toed ungulates (Artiodactyla), and the hippopotamus is more closely related to whales than to horses or rhinos.

### Giant-Panda-Bears — Giant Panda Placement
Cytochrome b sequences for 10 species in and around family Ursidae. Molecular data definitively placed the giant panda within the bears — resolving a long-standing debate about whether it was a bear, a relative of the red panda, or something else.

### Great-Apes-FOXP2 — FOXP2 Language Gene
FOXP2 protein sequences (~711–716 amino acids) for 9 species including humans, great apes, and the zebra finch. FOXP2 is implicated in human speech and language; the human protein differs from other great apes by only 2 amino acids. The zebra finch is included because FOXP2 is also essential for vocal learning in songbirds.

### HIV-Subtypes — HIV Evolutionary Origins
Gag polyprotein sequences (~500 amino acids) from reference strains of HIV-1 (subtypes A, B, C, D, G, and groups M, N, O), HIV-2 (groups A and B), and SIVcpz. HIV-1 and HIV-2 arose from independent transmissions of primate SIVs to humans; the tree makes these separate origins visible.

### Mitochondrial-Haplogroups — Human mtDNA Migration
HVR1 (Hypervariable Region 1, ~546 nt) sequences extracted from complete human mitochondrial genomes representing 13 major haplogroups. Because mitochondrial DNA is inherited maternally without recombination, the tree traces human migration out of Africa — from the deepest branch (haplogroup L0, San Bushmen, ~200,000 years ago) through the founding haplogroups of Indigenous Americans (A, B, C, D).

### UK-SARS-CoV-2 — SARS-CoV-2 Evolution
Spike protein sequences from 261 UK SARS-CoV-2 genomes sampled over every two-week period between November 2020 and March 2024 (three genomes per time point). Sample labels have the form `YYYY-MM-DD_XX`. Unlike the other datasets, this tree has a time axis: samples taken further apart in time should appear further apart in the tree.
