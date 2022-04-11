import { object, string, number } from 'yup';

export const materials = [
  {
    value: 1,
    label: "Music wire (ASTM No. A228)",
  },
  {
    value: 2,
    label: "Hard-drawn wire (ASTM No. A227)",
  },
  {
    value: 3,
    label: "Chrome-vanadium wire (ASTM No. A232)",
  },
  {
    value: 4,
    label: "Chrome-silicon wire (ASTM No. A401)",
  },
  {
    value: 5,
    label: "302 stainless wire (ASTM No. A313)",
  },
  {
    value: 6,
    label: "Phosphor-bronze wire (ASTM No. B159)",
  },
];

export const materials_labels = materials.map(mat => mat.label);

export const endTypes = [
    {
        value: 1,
        label: "Plain"
    },
    {
        value: 2,
        label: "Plain and ground"
    },
    {
        value: 3,
        label: "Squared or closed"
    },
    {
        value: 4,
        label: "Squared and ground"
    }
]

export const endTypes_labels = endTypes.map(obj => obj.label);


export const theSchema = object().shape({
  material: string().oneOf(materials_labels).required(),
  endType: string().oneOf(endTypes_labels).required(),
  wireDiameter_mm: number().positive().required(),
  OD_mm: number().positive().required(),
  L0_mm: number().positive().required(),
  Ls_mm: number().positive().required()
});

export const mainResultsTemplate = {
  pitch: "",
  nt: "",
  na: "",
  k: "",
  F_ls: "",
  n_ls: ""
};