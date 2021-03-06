class self.JSREPLEngine
  constructor: (unused_input, @output, @result, @error, sandbox, ready) ->
    @Python = sandbox.Python
    sandbox.print = (->)

    @output_buffer = []
    output_wrapper = (chr) =>
      if chr?
        @output_buffer.push chr
        output chr
    printOutput = makeUtf8Print(output_wrapper)

    @error_buffer = []
    printError = makeUtf8Print(output)
    bufferError = (chr) =>
      if chr?
        if @Python.isHandlingError
          @error_buffer.push String.fromCharCode chr
        else
          printError chr
    @Python.initialize null, printOutput, bufferError
    ready()

  Eval: (command) ->
    @error_buffer = []
    try
      result = @Python.eval encodeUtf8 command
      if result == undefined
        @error @error_buffer.join('') or 'Unknown error.'
      else
        @output @error_buffer.join ''
        @result result
    catch e
      @error 'Internal error: ' + e

  EasyLearnCode_Eval: (input) ->
    try
      if input.testScript
        @Python.eval encodeUtf8 input.testScript
      @error_buffer = []
      @output_buffer = []
      result = @Python.eval encodeUtf8 input.command
      error_str = @error_buffer.join ''
      if result == undefined
        @error @error_buffer.join('') or 'Unknown error.', input.type
      else
        @output error_str
        output_str = @output_buffer.join ''
        resultObj =
          result: result
          output: output_str
          code: input.command
          type: input.type
        @result resultObj
    catch e
      @error 'Internal error: ' + e, input.type

  # TODO(amasad): Try to capture return type?
  RawEval: (command) ->
    @Eval command

  GetNextLineIndent: (command) ->
    lines = command.split '\n'
    if lines.length == 0
      return 0
    else
      last_line = lines[lines.length - 1]
      indent = last_line.match(/^\s*/)[0]
      last_line = lines[lines.length - 1].replace /\s+$/, ''
      if last_line[last_line.length - 1] == ':'
        return 1
      else if indent.length and last_line[last_line.length - 1].length != 0
        return 0
      else
        return false