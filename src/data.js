import { object, string, number } from 'yup';

export const apiUrl = "https://bsthlri5j1.execute-api.us-east-1.amazonaws.com/springs_backend"

export const materials = [
	{
		value: 1,
		label: 'Music wire (ASTM No. A228)',
	},
	{
		value: 2,
		label: 'Hard-drawn wire (ASTM No. A227)',
	},
	{
		value: 3,
		label: 'Chrome-vanadium wire (ASTM No. A232)',
	},
	{
		value: 4,
		label: 'Chrome-silicon wire (ASTM No. A401)',
	},
	{
		value: 5,
		label: '302 stainless wire (ASTM No. A313)',
	},
	{
		value: 6,
		label: 'Phosphor-bronze wire (ASTM No. B159)',
	},
];

export const materials_labels = materials.map((mat) => mat.label);

export const endTypes = [
	{
		value: 1,
		label: 'Plain',
	},
	{
		value: 2,
		label: 'Plain and ground',
	},
	{
		value: 3,
		label: 'Squared or closed',
	},
	{
		value: 4,
		label: 'Squared and ground',
	},
];

export const endTypes_labels = endTypes.map((obj) => obj.label);

export const mainRequestSchema = object().shape({
	material: string().oneOf(materials_labels).required(),
	endType: string().oneOf(endTypes_labels).required(),
	wireDiameter_in: number().positive().required(),
	OD_in: number().positive().required(),
	L0_in: number().positive().required(),
	Ls_in: number().positive().required(),
});

export const mainResultsTemplate = {
	pitch_in_rev: '',
	nt_: '',
	na_: '',
	k_lbf_in: '',
	Fls_lbf: '',
	n_ls_: '',
};

export const staticRequestSchema = object().shape({
	material: string().oneOf(materials_labels).required(),
	endType: string().oneOf(endTypes_labels).required(),
	wireDiameter_in: number().positive().required(),
	OD_in: number().positive().required(),
	L0_in: number().positive().required(),
	Ls_in: number().positive().required(),

	Fs_lbf: number().required(),
});

export const staticResultsTemplate = {
	n_s_: '',
};

export const fatigueRequestSchema = object().shape({
	material: string().oneOf(materials_labels).required(),
	endType: string().oneOf(endTypes_labels).required(),
	wireDiameter_in: number().positive().required(),
	OD_in: number().positive().required(),
	L0_in: number().positive().required(),
	Ls_in: number().positive().required(),

	F_max_lbf: number().required(),
	F_min_lbf: number().required(),
});

export const fatigueResultsTemplate = {
	n_f_: '',
};
