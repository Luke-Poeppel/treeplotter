def _prepare_docs_and_screenshot(path, serialized_tree, logger):
	with open("tree.json", "w") as json_file:
		json.dump(serialized_tree, json_file)

	logger.info("-> Copying .js files...")
	for this_file in os.listdir(treant_templates):
		shutil.copyfile(treant_templates + "/" + this_file, path + "/" + this_file)

	logger.info("-> Running browserify...")
	parse_data_file = "/".join([path, "parse_data.js"])
	browserified_file = "/".join([path, "bundle.js"])
	os.system(f"browserify {parse_data_file} -o {browserified_file}")

	logger.info("-> Creating webshot with R...")
	webshot_string = "webshot::webshot(url={0}, file={1}, zoom=3, selector={2})".format(
		"'" + path + "/index.html" + "'",
		"'" + path + "/shot.png" + "'",
		"'" + ".Treant" + "'"
	)
	subprocess.call(
		[
			f"""Rscript -e "{webshot_string}" """
		],
		shell=True
	)

def create_tree_diagram(FragmentTree, path=None, verbose=False):
	"""
	This function creates a visualization of a given :obj:`~decitala.trees.FragmentTree`
	using the Treant.js library. If a path is provided, all the files will be stored there. Otherwise,
	they will be stored in a tempfile for the display.

	:param `~decitala.trees.FragmentTree` FragmentTree: A Fragment tree
	:param str path: Path to the folder where the visualization will be optionally stored.
					Default is `None`.
	:return: A folder at the provided path containing an index.html file which has a visualization
			of the provided :obj:`~decitala.trees.FragmentTree`.
	"""
	if verbose:
		logger = get_logger(name=__name__, print_to_console=True)
	else:
		logger = get_logger(name=__name__, print_to_console=False)

	stupid_tree = trees.NaryTree()
	if FragmentTree.rep_type == "ratio":
		root = trees.NaryTree().Node(value=1.0, name=None)
		for this_fragment in FragmentTree.sorted_data:
			fragment_list = this_fragment.successive_ratio_array().tolist()
			root.add_path_of_children(fragment_list, this_fragment.name)
	else:
		root = trees.NaryTree().Node(value=0.0, name=None)
		for this_fragment in FragmentTree.sorted_data:
			fragment_list = this_fragment.successive_difference_array().tolist()
			root.add_path_of_children(fragment_list, this_fragment.name)

	stupid_tree.root = root
	serialized = stupid_tree.serialize(for_treant=True)

	logger.info("-> Creating directory and writing tree to JSON...")
	if path is not None:
		os.mkdir(path)
		os.chdir(path)
		_prepare_docs_and_screenshot(path, serialized_tree=serialized, logger=logger)
		logger.info("Done ✔")
		return path
	else:
		with tempfile.TemporaryDirectory() as tmpdir:
			os.chdir(tmpdir)
			_prepare_docs_and_screenshot(tmpdir, serialized_tree=serialized, logger=logger)
			logger.info("Done ✔")
			with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
				shutil.copyfile(tmpdir + "/shot.png", tmpfile.name)
				return tmpfile.name