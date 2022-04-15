import { object, string, number } from 'yup';

export const apiUrl = "https://bsthlri5j1.execute-api.us-east-1.amazonaws.com/springs_backend"

export const materials = [
	{
		value: 'A228',
		label: 'Music wire (ASTM No. A228)',
	},
	{
		value: 'A227',
		label: 'Hard-drawn wire (ASTM No. A227)',
	},
	{
		value: 'A232',
		label: 'Chrome-vanadium wire (ASTM No. A232)',
	},
	{
		value: 'A401',
		label: 'Chrome-silicon wire (ASTM No. A401)',
	},
	{
		value: 'A313',
		label: '302 stainless wire (ASTM No. A313)',
	},
	{
		value: 'B159',
		label: 'Phosphor-bronze wire (ASTM No. B159)',
	},
];

const materials_values = materials.map((mat) => mat.value);

export const endTypes = [
	{
		value: 'plain',
		label: 'Plain',
	},
	{
		value: 'plainAndGround',
		label: 'Plain and ground',
	},
	{
		value: 'squaredOrClosed',
		label: 'Squared or closed',
	},
	{
		value: 'squaredAndGround',
		label: 'Squared and ground',
	},
];

const endTypes_values = endTypes.map((obj) => obj.value);

export const mainRequestSchema = object().shape({
	material: string().oneOf(materials_values).required(),
	endType: string().oneOf(endTypes_values).required(),
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
	fShut_lbf: '',
	nShut_: '',
};

export const staticRequestSchema = object().shape({
	material: string().oneOf(materials_values).required(),
	endType: string().oneOf(endTypes_values).required(),
	wireDiameter_in: number().positive().required(),
	OD_in: number().positive().required(),
	L0_in: number().positive().required(),
	Ls_in: number().positive().required(),

	Fstatic_lbf: number().required(),
});

export const staticResultsTemplate = {
	nStatic_: '',
};

export const fatigueRequestSchema = object().shape({
	material: string().oneOf(materials_values).required(),
	endType: string().oneOf(endTypes_values).required(),
	wireDiameter_in: number().positive().required(),
	OD_in: number().positive().required(),
	L0_in: number().positive().required(),
	Ls_in: number().positive().required(),

	F_max_lbf: number().required(),
	F_min_lbf: number().required(),
});

export const fatigueResultsTemplate = {
	nFatigue_: '',
};
