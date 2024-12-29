Directory structure:
└── openai-openai-python/
    ├── api.md
    ├── tests/
    │   ├── sample_file.txt
    │   ├── api_resources/
    │   │   ├── test_completions.py
    │   │   ├── audio/
    │   │   │   ├── test_transcriptions.py
    │   │   │   ├── __init__.py
    │   │   │   ├── test_speech.py
    │   │   │   └── test_translations.py
    │   │   ├── test_moderations.py
    │   │   ├── test_images.py
    │   │   ├── test_batches.py
    │   │   ├── __init__.py
    │   │   ├── test_files.py
    │   │   ├── uploads/
    │   │   │   ├── test_parts.py
    │   │   │   └── __init__.py
    │   │   ├── test_uploads.py
    │   │   ├── test_models.py
    │   │   ├── beta/
    │   │   │   ├── threads/
    │   │   │   │   ├── runs/
    │   │   │   │   │   ├── test_steps.py
    │   │   │   │   │   └── __init__.py
    │   │   │   │   ├── test_messages.py
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── test_runs.py
    │   │   │   ├── realtime/
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── test_sessions.py
    │   │   │   ├── vector_stores/
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── test_files.py
    │   │   │   │   └── test_file_batches.py
    │   │   │   ├── test_threads.py
    │   │   │   ├── __init__.py
    │   │   │   ├── test_assistants.py
    │   │   │   ├── test_realtime.py
    │   │   │   └── test_vector_stores.py
    │   │   ├── chat/
    │   │   │   ├── test_completions.py
    │   │   │   └── __init__.py
    │   │   ├── test_embeddings.py
    │   │   └── fine_tuning/
    │   │       ├── __init__.py
    │   │       ├── jobs/
    │   │       │   ├── __init__.py
    │   │       │   └── test_checkpoints.py
    │   │       └── test_jobs.py
    │   ├── test_deepcopy.py
    │   ├── test_client.py
    │   ├── __init__.py
    │   ├── test_required_args.py
    │   ├── test_files.py
    │   ├── lib/
    │   │   ├── __init__.py
    │   │   ├── test_assistants.py
    │   │   ├── test_old_api.py
    │   │   ├── test_pydantic.py
    │   │   ├── test_audio.py
    │   │   ├── chat/
    │   │   │   ├── test_completions.py
    │   │   │   ├── _utils.py
    │   │   │   ├── __init__.py
    │   │   │   └── test_completions_streaming.py
    │   │   ├── schema_types/
    │   │   │   └── query.py
    │   │   └── test_azure.py
    │   ├── test_legacy_response.py
    │   ├── test_qs.py
    │   ├── conftest.py
    │   ├── test_response.py
    │   ├── test_streaming.py
    │   ├── test_module_client.py
    │   ├── test_utils/
    │   │   ├── test_logging.py
    │   │   ├── test_typing.py
    │   │   └── test_proxy.py
    │   ├── test_models.py
    │   ├── test_extract_files.py
    │   ├── utils.py
    │   └── test_transform.py
    ├── CHANGELOG.md
    ├── scripts/
    │   ├── bootstrap
    │   ├── lint
    │   ├── format
    │   ├── test
    │   ├── mock
    │   └── utils/
    │       └── ruffen-docs.py
    ├── .github/
    │   ├── workflows/
    │   │   ├── ci.yml
    │   │   ├── create-releases.yml
    │   │   ├── publish-pypi.yml
    │   │   └── release-doctor.yml
    │   ├── pull_request_template.md
    │   ├── CODEOWNERS
    │   └── ISSUE_TEMPLATE/
    │       ├── feature_request.yml
    │       ├── config.yml
    │       └── bug_report.yml
    ├── helpers.md
    ├── .release-please-manifest.json
    ├── bin/
    │   ├── check-release-environment
    │   └── publish-pypi
    ├── Brewfile
    ├── .stats.yml
    ├── .python-version
    ├── .inline-snapshot/
    │   └── external/
    │       ├── 173417d553406f034f643e5db3f8d591fb691ebac56f5ae39a22cc7d455c5353.bin
    │       ├── c6aa7e397b7123c3501f25df3a05d4daf7e8ad6d61ffa406ab5361fe36a8d5b1.bin
    │       ├── 7e5ea4d12e7cc064399b6631415e65923f182256b6e6b752950a3aaa2ad2320a.bin
    │       ├── e2aad469b71d1d4894ff833ea147020a9d875eb7ce644a0ff355581690a4cbfd.bin
    │       ├── .gitignore
    │       ├── 2018feb66ae13fcf5333d61b95849decc68d3f63bd38172889367e1afb1e04f7.bin
    │       ├── a247c49c5fcd492bfb7a02a3306ad615ed8d8f649888ebfddfbc3ee151f44d46.bin
    │       ├── d615580118391ee13492193e3a8bb74642d23ac1ca13fe37cb6e889b66f759f6.bin
    │       ├── a491adda08c3d4fde95f5b2ee3f60f7f745f1a56d82e62f58031cc2add502380.bin
    │       ├── 83b060bae42eb41c4f1edbb7c1542b954b37d9dfd1910b964ddebc9677e6ae85.bin
    │       ├── f82268f2fefd5cfbc7eeb59c297688be2f6ca0849a6e4f17851b517310841d9b.bin
    │       ├── 569c877e69429d4cbc1577d2cd6dd33878095c68badc6b6654a69769b391a1c1.bin
    │       └── 4cc50a6135d254573a502310e6af1246f55edb6ad95fa24059f160996b68866d.bin
    ├── requirements.lock
    ├── pyproject.toml
    ├── .devcontainer/
    │   ├── devcontainer.json
    │   └── Dockerfile
    ├── examples/
    │   ├── .keep
    │   ├── parsing_stream.py
    │   ├── module_client.py
    │   ├── assistant_stream_helpers.py
    │   ├── realtime/
    │   │   ├── push_to_talk_app.py
    │   │   └── audio_util.py
    │   ├── audio.py
    │   ├── async_demo.py
    │   ├── parsing_tools_stream.py
    │   ├── demo.py
    │   ├── parsing_tools.py
    │   ├── assistant.py
    │   ├── picture.py
    │   ├── assistant_stream.py
    │   ├── parsing.py
    │   ├── generate_file.sh
    │   ├── uploads.py
    │   ├── azure.py
    │   ├── azure_ad.py
    │   └── streaming.py
    ├── requirements-dev.lock
    ├── SECURITY.md
    ├── noxfile.py
    ├── mypy.ini
    ├── LICENSE
    ├── README.md
    ├── release-please-config.json
    ├── CONTRIBUTING.md
    └── src/
        └── openai/
            ├── _resource.py
            ├── __main__.py
            ├── _utils/
            │   ├── _sync.py
            │   ├── _logs.py
            │   ├── _transform.py
            │   ├── _utils.py
            │   ├── __init__.py
            │   ├── _proxy.py
            │   ├── _typing.py
            │   ├── _streams.py
            │   └── _reflection.py
            ├── _module_client.py
            ├── _extras/
            │   ├── _common.py
            │   ├── __init__.py
            │   ├── numpy_proxy.py
            │   └── pandas_proxy.py
            ├── pagination.py
            ├── resources/
            │   ├── moderations.py
            │   ├── audio/
            │   │   ├── audio.py
            │   │   ├── speech.py
            │   │   ├── __init__.py
            │   │   ├── transcriptions.py
            │   │   └── translations.py
            │   ├── models.py
            │   ├── completions.py
            │   ├── __init__.py
            │   ├── embeddings.py
            │   ├── uploads/
            │   │   ├── __init__.py
            │   │   ├── parts.py
            │   │   └── uploads.py
            │   ├── files.py
            │   ├── images.py
            │   ├── batches.py
            │   ├── beta/
            │   │   ├── threads/
            │   │   │   ├── runs/
            │   │   │   │   ├── __init__.py
            │   │   │   │   ├── runs.py
            │   │   │   │   └── steps.py
            │   │   │   ├── threads.py
            │   │   │   ├── __init__.py
            │   │   │   └── messages.py
            │   │   ├── realtime/
            │   │   │   ├── __init__.py
            │   │   │   ├── realtime.py
            │   │   │   └── sessions.py
            │   │   ├── vector_stores/
            │   │   │   ├── __init__.py
            │   │   │   ├── file_batches.py
            │   │   │   ├── files.py
            │   │   │   └── vector_stores.py
            │   │   ├── assistants.py
            │   │   ├── __init__.py
            │   │   ├── beta.py
            │   │   └── chat/
            │   │       ├── chat.py
            │   │       ├── completions.py
            │   │       └── __init__.py
            │   ├── chat/
            │   │   ├── chat.py
            │   │   ├── completions.py
            │   │   └── __init__.py
            │   └── fine_tuning/
            │       ├── __init__.py
            │       ├── jobs/
            │       │   ├── __init__.py
            │       │   ├── jobs.py
            │       │   └── checkpoints.py
            │       └── fine_tuning.py
            ├── _legacy_response.py
            ├── _constants.py
            ├── cli/
            │   ├── _progress.py
            │   ├── _cli.py
            │   ├── _utils.py
            │   ├── __init__.py
            │   ├── _errors.py
            │   ├── _models.py
            │   ├── _api/
            │   │   ├── audio.py
            │   │   ├── models.py
            │   │   ├── completions.py
            │   │   ├── __init__.py
            │   │   ├── _main.py
            │   │   ├── files.py
            │   │   ├── chat/
            │   │   │   ├── completions.py
            │   │   │   └── __init__.py
            │   │   └── image.py
            │   └── _tools/
            │       ├── __init__.py
            │       ├── fine_tunes.py
            │       ├── _main.py
            │       └── migrate.py
            ├── __init__.py
            ├── _qs.py
            ├── _compat.py
            ├── lib/
            │   ├── .keep
            │   ├── streaming/
            │   │   ├── _assistants.py
            │   │   ├── __init__.py
            │   │   ├── _deltas.py
            │   │   └── chat/
            │   │       ├── _completions.py
            │   │       ├── __init__.py
            │   │       ├── _events.py
            │   │       └── _types.py
            │   ├── _pydantic.py
            │   ├── _validators.py
            │   ├── __init__.py
            │   ├── _parsing/
            │   │   ├── _completions.py
            │   │   └── __init__.py
            │   ├── azure.py
            │   ├── _tools.py
            │   └── _old_api.py
            ├── _base_client.py
            ├── _exceptions.py
            ├── _types.py
            ├── _response.py
            ├── _client.py
            ├── _files.py
            ├── _version.py
            ├── version.py
            ├── py.typed
            ├── _models.py
            ├── _streaming.py
            └── types/
                ├── audio_model.py
                ├── create_embedding_response.py
                ├── batch_list_params.py
                ├── file_purpose.py
                ├── moderation_create_params.py
                ├── moderation_multi_modal_input_param.py
                ├── upload_complete_params.py
                ├── audio/
                │   ├── transcription_create_response.py
                │   ├── transcription_create_params.py
                │   ├── transcription.py
                │   ├── speech_create_params.py
                │   ├── translation.py
                │   ├── translation_create_response.py
                │   ├── __init__.py
                │   ├── translation_create_params.py
                │   ├── translation_verbose.py
                │   ├── transcription_word.py
                │   ├── speech_model.py
                │   ├── transcription_verbose.py
                │   └── transcription_segment.py
                ├── moderation_create_response.py
                ├── moderation_image_url_input_param.py
                ├── embedding_model.py
                ├── file_content.py
                ├── images_response.py
                ├── image_generate_params.py
                ├── file_deleted.py
                ├── __init__.py
                ├── chat_model.py
                ├── file_list_params.py
                ├── batch_request_counts.py
                ├── image_create_variation_params.py
                ├── completion_usage.py
                ├── shared_params/
                │   ├── function_definition.py
                │   ├── __init__.py
                │   ├── response_format_json_object.py
                │   ├── response_format_json_schema.py
                │   ├── response_format_text.py
                │   └── function_parameters.py
                ├── batch_create_params.py
                ├── shared/
                │   ├── function_definition.py
                │   ├── __init__.py
                │   ├── response_format_json_object.py
                │   ├── response_format_json_schema.py
                │   ├── error_object.py
                │   ├── response_format_text.py
                │   └── function_parameters.py
                ├── image_model.py
                ├── batch_error.py
                ├── completion_create_params.py
                ├── uploads/
                │   ├── upload_part.py
                │   ├── __init__.py
                │   └── part_create_params.py
                ├── completion.py
                ├── batch.py
                ├── completion_choice.py
                ├── model_deleted.py
                ├── moderation_model.py
                ├── moderation.py
                ├── image_edit_params.py
                ├── beta/
                │   ├── assistant_stream_event.py
                │   ├── assistant_response_format_option.py
                │   ├── thread_deleted.py
                │   ├── threads/
                │   │   ├── required_action_function_tool_call.py
                │   │   ├── message_list_params.py
                │   │   ├── image_file_delta_block.py
                │   │   ├── runs/
                │   │   │   ├── code_interpreter_tool_call.py
                │   │   │   ├── tool_call_delta.py
                │   │   │   ├── code_interpreter_output_image.py
                │   │   │   ├── run_step_delta.py
                │   │   │   ├── run_step.py
                │   │   │   ├── run_step_delta_event.py
                │   │   │   ├── tool_call_delta_object.py
                │   │   │   ├── message_creation_step_details.py
                │   │   │   ├── __init__.py
                │   │   │   ├── step_retrieve_params.py
                │   │   │   ├── code_interpreter_logs.py
                │   │   │   ├── function_tool_call_delta.py
                │   │   │   ├── function_tool_call.py
                │   │   │   ├── run_step_delta_message_delta.py
                │   │   │   ├── tool_call.py
                │   │   │   ├── file_search_tool_call_delta.py
                │   │   │   ├── run_step_include.py
                │   │   │   ├── step_list_params.py
                │   │   │   ├── file_search_tool_call.py
                │   │   │   ├── code_interpreter_tool_call_delta.py
                │   │   │   └── tool_calls_step_details.py
                │   │   ├── image_file_delta.py
                │   │   ├── text_delta_block.py
                │   │   ├── image_url_delta.py
                │   │   ├── message_create_params.py
                │   │   ├── run_create_params.py
                │   │   ├── image_file.py
                │   │   ├── message_update_params.py
                │   │   ├── annotation_delta.py
                │   │   ├── __init__.py
                │   │   ├── image_url_param.py
                │   │   ├── file_path_annotation.py
                │   │   ├── text_content_block.py
                │   │   ├── run_update_params.py
                │   │   ├── message_content_part_param.py
                │   │   ├── image_url_delta_block.py
                │   │   ├── annotation.py
                │   │   ├── image_url.py
                │   │   ├── refusal_delta_block.py
                │   │   ├── run_status.py
                │   │   ├── text_delta.py
                │   │   ├── image_url_content_block.py
                │   │   ├── message_content.py
                │   │   ├── run_list_params.py
                │   │   ├── text_content_block_param.py
                │   │   ├── message_deleted.py
                │   │   ├── file_path_delta_annotation.py
                │   │   ├── image_file_param.py
                │   │   ├── message.py
                │   │   ├── file_citation_delta_annotation.py
                │   │   ├── run_submit_tool_outputs_params.py
                │   │   ├── text.py
                │   │   ├── refusal_content_block.py
                │   │   ├── image_file_content_block_param.py
                │   │   ├── image_url_content_block_param.py
                │   │   ├── message_delta_event.py
                │   │   ├── message_content_delta.py
                │   │   ├── file_citation_annotation.py
                │   │   ├── message_delta.py
                │   │   ├── run.py
                │   │   └── image_file_content_block.py
                │   ├── realtime/
                │   │   ├── response_function_call_arguments_done_event.py
                │   │   ├── response_audio_transcript_delta_event.py
                │   │   ├── input_audio_buffer_clear_event.py
                │   │   ├── session_create_params.py
                │   │   ├── realtime_response_status.py
                │   │   ├── conversation_item_input_audio_transcription_completed_event.py
                │   │   ├── input_audio_buffer_speech_stopped_event.py
                │   │   ├── conversation_item_truncate_event.py
                │   │   ├── session_updated_event.py
                │   │   ├── input_audio_buffer_speech_started_event.py
                │   │   ├── input_audio_buffer_cleared_event.py
                │   │   ├── input_audio_buffer_clear_event_param.py
                │   │   ├── realtime_response.py
                │   │   ├── response_function_call_arguments_delta_event.py
                │   │   ├── conversation_item_content.py
                │   │   ├── response_audio_transcript_done_event.py
                │   │   ├── realtime_server_event.py
                │   │   ├── input_audio_buffer_commit_event_param.py
                │   │   ├── __init__.py
                │   │   ├── input_audio_buffer_commit_event.py
                │   │   ├── response_created_event.py
                │   │   ├── session_update_event_param.py
                │   │   ├── response_content_part_added_event.py
                │   │   ├── input_audio_buffer_committed_event.py
                │   │   ├── realtime_connect_params.py
                │   │   ├── realtime_client_event_param.py
                │   │   ├── session_create_response.py
                │   │   ├── session_created_event.py
                │   │   ├── response_audio_delta_event.py
                │   │   ├── response_audio_done_event.py
                │   │   ├── response_text_delta_event.py
                │   │   ├── conversation_item_param.py
                │   │   ├── conversation_created_event.py
                │   │   ├── conversation_item_create_event_param.py
                │   │   ├── rate_limits_updated_event.py
                │   │   ├── response_cancel_event.py
                │   │   ├── response_cancel_event_param.py
                │   │   ├── conversation_item_deleted_event.py
                │   │   ├── conversation_item_delete_event.py
                │   │   ├── error_event.py
                │   │   ├── session_update_event.py
                │   │   ├── conversation_item_input_audio_transcription_failed_event.py
                │   │   ├── response_done_event.py
                │   │   ├── response_output_item_added_event.py
                │   │   ├── response_output_item_done_event.py
                │   │   ├── conversation_item_content_param.py
                │   │   ├── conversation_item_created_event.py
                │   │   ├── conversation_item_create_event.py
                │   │   ├── realtime_response_usage.py
                │   │   ├── response_text_done_event.py
                │   │   ├── input_audio_buffer_append_event.py
                │   │   ├── conversation_item_truncated_event.py
                │   │   ├── input_audio_buffer_append_event_param.py
                │   │   ├── realtime_client_event.py
                │   │   ├── session.py
                │   │   ├── conversation_item.py
                │   │   ├── response_content_part_done_event.py
                │   │   ├── response_create_event.py
                │   │   ├── response_create_event_param.py
                │   │   ├── conversation_item_delete_event_param.py
                │   │   └── conversation_item_truncate_event_param.py
                │   ├── thread_create_and_run_params.py
                │   ├── static_file_chunking_strategy_object.py
                │   ├── vector_stores/
                │   │   ├── file_batch_list_files_params.py
                │   │   ├── vector_store_file_deleted.py
                │   │   ├── vector_store_file.py
                │   │   ├── __init__.py
                │   │   ├── file_list_params.py
                │   │   ├── file_batch_create_params.py
                │   │   ├── file_create_params.py
                │   │   └── vector_store_file_batch.py
                │   ├── vector_store_create_params.py
                │   ├── assistant_tool.py
                │   ├── file_chunking_strategy_param.py
                │   ├── code_interpreter_tool_param.py
                │   ├── assistant.py
                │   ├── assistant_tool_param.py
                │   ├── function_tool_param.py
                │   ├── auto_file_chunking_strategy_param.py
                │   ├── vector_store_deleted.py
                │   ├── __init__.py
                │   ├── thread_create_params.py
                │   ├── static_file_chunking_strategy.py
                │   ├── code_interpreter_tool.py
                │   ├── thread_update_params.py
                │   ├── assistant_tool_choice_option.py
                │   ├── assistant_response_format_option_param.py
                │   ├── assistant_update_params.py
                │   ├── thread.py
                │   ├── assistant_tool_choice_function.py
                │   ├── file_search_tool_param.py
                │   ├── static_file_chunking_strategy_param.py
                │   ├── assistant_list_params.py
                │   ├── vector_store.py
                │   ├── assistant_tool_choice_param.py
                │   ├── file_search_tool.py
                │   ├── assistant_create_params.py
                │   ├── other_file_chunking_strategy_object.py
                │   ├── chat/
                │   │   └── __init__.py
                │   ├── function_tool.py
                │   ├── vector_store_list_params.py
                │   ├── assistant_deleted.py
                │   ├── assistant_tool_choice.py
                │   ├── vector_store_update_params.py
                │   ├── assistant_tool_choice_function_param.py
                │   ├── assistant_tool_choice_option_param.py
                │   └── file_chunking_strategy.py
                ├── chat/
                │   ├── chat_completion_modality.py
                │   ├── chat_completion_content_part_text_param.py
                │   ├── chat_completion_message_tool_call.py
                │   ├── chat_completion_tool_message_param.py
                │   ├── chat_completion_audio_param.py
                │   ├── parsed_chat_completion.py
                │   ├── chat_completion_message.py
                │   ├── chat_completion_named_tool_choice_param.py
                │   ├── chat_completion_tool_choice_option_param.py
                │   ├── __init__.py
                │   ├── chat_completion_message_param.py
                │   ├── chat_completion_content_part_input_audio_param.py
                │   ├── chat_completion_function_call_option_param.py
                │   ├── chat_completion_content_part_image_param.py
                │   ├── chat_completion_content_part_param.py
                │   ├── chat_completion_chunk.py
                │   ├── completion_create_params.py
                │   ├── chat_completion_token_logprob.py
                │   ├── chat_completion_reasoning_effort.py
                │   ├── chat_completion_message_tool_call_param.py
                │   ├── chat_completion_audio.py
                │   ├── chat_completion_tool_param.py
                │   ├── chat_completion_system_message_param.py
                │   ├── chat_completion_stream_options_param.py
                │   ├── chat_completion_assistant_message_param.py
                │   ├── chat_completion_role.py
                │   ├── chat_completion_user_message_param.py
                │   ├── parsed_function_tool_call.py
                │   ├── chat_completion_content_part_refusal_param.py
                │   ├── chat_completion_developer_message_param.py
                │   ├── chat_completion_prediction_content_param.py
                │   ├── chat_completion.py
                │   └── chat_completion_function_message_param.py
                ├── upload.py
                ├── embedding.py
                ├── upload_create_params.py
                ├── embedding_create_params.py
                ├── file_object.py
                ├── audio_response_format.py
                ├── websocket_connection_options.py
                ├── moderation_text_input_param.py
                ├── image.py
                ├── fine_tuning/
                │   ├── job_list_params.py
                │   ├── fine_tuning_job.py
                │   ├── __init__.py
                │   ├── fine_tuning_job_wandb_integration.py
                │   ├── fine_tuning_job_integration.py
                │   ├── fine_tuning_job_event.py
                │   ├── jobs/
                │   │   ├── __init__.py
                │   │   ├── fine_tuning_job_checkpoint.py
                │   │   └── checkpoint_list_params.py
                │   ├── job_create_params.py
                │   ├── fine_tuning_job_wandb_integration_object.py
                │   └── job_list_events_params.py
                ├── model.py
                └── file_create_params.py


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
File: /README.md
================================================
# OpenAI Python API library

[![PyPI version](https://img.shields.io/pypi/v/openai.svg)](https://pypi.org/project/openai/)

The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated from our [OpenAPI specification](https://github.com/openai/openai-openapi) with [Stainless](https://stainlessapi.com/).

## Documentation

The REST API documentation can be found on [platform.openai.com](https://platform.openai.com/docs). The full API of this library can be found in [api.md](api.md).

## Installation

> [!IMPORTANT]
> The SDK was rewritten in v1, which was released November 6th 2023. See the [v1 migration guide](https://github.com/openai/openai-python/discussions/742), which includes scripts to automatically update your code.

```sh
# install from PyPI
pip install openai
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `OPENAI_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.

### Vision

With a hosted image:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"{img_url}"},
                },
            ],
        }
    ],
)
```

With the image as a base64 encoded string:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{img_type};base64,{img_b64_str}"},
                },
            ],
        }
    ],
)
```

### Polling Helpers

When interacting with the API some actions such as starting a Run and adding files to vector stores are asynchronous and take time to complete. The SDK includes
helper functions which will poll the status until it reaches a terminal state and then return the resulting object.
If an API method results in an action that could benefit from polling there will be a corresponding version of the
method ending in '\_and_poll'.

For instance to create a Run and poll until it reaches a terminal state you can run:

```python
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
)
```

More information on the lifecycle of a Run can be found in the [Run Lifecycle Documentation](https://platform.openai.com/docs/assistants/how-it-works/run-lifecycle)

### Bulk Upload Helpers

When creating and interacting with vector stores, you can use polling helpers to monitor the status of operations.
For convenience, we also provide a bulk upload helper to allow you to simultaneously upload several files at once.

```python
sample_files = [Path("sample-paper.pdf"), ...]

batch = await client.vector_stores.file_batches.upload_and_poll(
    store.id,
    files=sample_files,
)
```

### Streaming Helpers

The SDK also includes helpers to process streams and handle incoming events.

```python
with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
) as stream:
    for event in stream:
        # Print the text from text delta events
        if event.type == "thread.message.delta" and event.data.delta.content:
            print(event.data.delta.content[0].text)
```

More information on streaming helpers can be found in the dedicated documentation: [helpers.md](helpers.md)

## Async usage

Simply import `AsyncOpenAI` instead of `OpenAI` and use `await` with each API call:

```python
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-4o",
    )


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Streaming responses

We provide support for streaming responses using Server Side Events (SSE).

```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

The async client uses the exact same interface.

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main():
    stream = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())
```

## Module-level client

> [!IMPORTANT]
> We highly recommend instantiating client instances instead of relying on the global client.

We also expose a global client instance that is accessible in a similar fashion to versions prior to v1.

```py
import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = '...'

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://..."
openai.default_headers = {"x-foo": "true"}

completion = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.choices[0].message.content)
```

The API is the exact same as the standard client instance-based API.

This is intended to be used within REPLs or notebooks for faster iteration, **not** in application code.

We recommend that you always instantiate a client (e.g., with `client = OpenAI()`) in application code because:

- It can be difficult to reason about where client options are configured
- It's not possible to change certain client options without potentially causing race conditions
- It's harder to mock for testing purposes
- It's not possible to control cleanup of network connections

## Realtime API beta

The Realtime API enables you to build low-latency, multi-modal conversational experiences. It currently supports text and audio as both input and output, as well as [function calling](https://platform.openai.com/docs/guides/function-calling) through a WebSocket connection.

Under the hood the SDK uses the [`websockets`](https://websockets.readthedocs.io/en/stable/) library to manage connections.

The Realtime API works through a combination of client-sent events and server-sent events. Clients can send events to do things like update session configuration or send text and audio inputs. Server events confirm when audio responses have completed, or when a text response from the model has been received. A full event reference can be found [here](platform.openai.com/docs/api-reference/realtime-client-events) and a guide can be found [here](https://platform.openai.com/docs/guides/realtime).

Basic text based example:

```py
import asyncio
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI()

    async with client.beta.realtime.connect(model="gpt-4o-realtime-preview-2024-10-01") as connection:
        await connection.session.update(session={'modalities': ['text']})

        await connection.conversation.item.create(
            item={
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": "Say hello!"}],
            }
        )
        await connection.response.create()

        async for event in connection:
            if event.type == 'response.text.delta':
                print(event.delta, flush=True, end="")

            elif event.type == 'response.text.done':
                print()

            elif event.type == "response.done":
                break

asyncio.run(main())
```

However the real magic of the Realtime API is handling audio inputs / outputs, see this example [TUI script](https://github.com/openai/openai-python/blob/main/examples/realtime/push_to_talk_app.py) for a fully fledged example.

### Realtime error handling

Whenever an error occurs, the Realtime API will send an [`error` event](https://platform.openai.com/docs/guides/realtime/realtime-api-beta#handling-errors) and the connection will stay open and remain usable. This means you need to handle it yourself, as *no errors are raised directly* by the SDK when an `error` event comes in.

```py
client = AsyncOpenAI()

async with client.beta.realtime.connect(model="gpt-4o-realtime-preview-2024-10-01") as connection:
    ...
    async for event in connection:
        if event.type == 'error':
            print(event.error.type)
            print(event.error.code)
            print(event.error.event_id)
            print(event.error.message)
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Pagination

List methods in the OpenAI API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
from openai import OpenAI

client = OpenAI()

all_jobs = []
# Automatically fetches more pages as needed.
for job in client.fine_tuning.jobs.list(
    limit=20,
):
    # Do something with job here
    all_jobs.append(job)
print(all_jobs)
```

Or, asynchronously:

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main() -> None:
    all_jobs = []
    # Iterate through items across all pages, issuing requests as needed.
    async for job in client.fine_tuning.jobs.list(
        limit=20,
    ):
        all_jobs.append(job)
    print(all_jobs)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.fine_tuning.jobs.list(
    limit=20,
)
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await client.fine_tuning.jobs.list(
    limit=20,
)

print(f"next page cursor: {first_page.after}")  # => "next page cursor: ..."
for job in first_page.data:
    print(job.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you generate an example json object describing a fruit?",
        }
    ],
    model="gpt-4o",
    response_format={"type": "json_object"},
)
```

## File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

client.files.create(
    file=Path("input.jsonl"),
    purpose="fine-tune",
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `openai.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `openai.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `openai.APIError`.

```python
import openai
from openai import OpenAI

client = OpenAI()

try:
    client.fine_tuning.jobs.create(
        model="gpt-4o",
        training_file="file-abc123",
    )
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

## Request IDs

> For more information on debugging requests, see [these docs](https://platform.openai.com/docs/api-reference/debugging-requests)

All object responses in the SDK provide a `_request_id` property which is added from the `x-request-id` response header so that you can quickly log failing requests and report them back to OpenAI.

```python
completion = await client.chat.completions.create(
    messages=[{"role": "user", "content": "Say this is a test"}], model="gpt-4"
)
print(completion._request_id)  # req_123
```

Note that unlike other properties that use an `_` prefix, the `_request_id` property
*is* public. Unless documented otherwise, *all* other `_` prefix properties,
methods and modules are *private*.


### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I get the name of the current day in JavaScript?",
        }
    ],
    model="gpt-4o",
)
```

### Timeouts

By default requests time out after 10 minutes. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # 20 seconds (default is 10 minutes)
    timeout=20.0,
)

# More granular control:
client = OpenAI(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I list all files in a directory using Python?",
        }
    ],
    model="gpt-4o",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `OPENAI_LOG` to `info`.

```shell
$ export OPENAI_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-4o",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
```

These methods return an [`LegacyAPIResponse`](https://github.com/openai/openai-python/tree/main/src/openai/_legacy_response.py) object. This is a legacy class as we're changing it slightly in the next major version.

For the sync client this will mostly be the same with the exception
of `content` & `text` will be methods instead of properties. In the
async client, all methods will be async.

A migration script will be provided & the migration in general should
be smooth.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

As such, `.with_streaming_response` methods return a different [`APIResponse`](https://github.com/openai/openai-python/tree/main/src/openai/_response.py) object, and the async client returns an [`AsyncAPIResponse`](https://github.com/openai/openai-python/tree/main/src/openai/_response.py) object.

```python
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) will be respected when making this
request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from openai import OpenAI, DefaultHttpxClient

client = OpenAI(
    # Or use the `OPENAI_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083/v1",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from openai import OpenAI

with OpenAI() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Microsoft Azure OpenAI

To use this library with [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview), use the `AzureOpenAI`
class instead of the `OpenAI` class.

> [!IMPORTANT]
> The Azure API shape differs from the core API shape which means that the static types for responses / params
> won't always be correct.

```py
from openai import AzureOpenAI

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    # https://learn.microsoft.com/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-07-01-preview",
    # https://learn.microsoft.com/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-endpoint.openai.azure.com",
)

completion = client.chat.completions.create(
    model="deployment-name",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())
```

In addition to the options provided in the base `OpenAI` client, the following options are provided:

- `azure_endpoint` (or the `AZURE_OPENAI_ENDPOINT` environment variable)
- `azure_deployment`
- `api_version` (or the `OPENAI_API_VERSION` environment variable)
- `azure_ad_token` (or the `AZURE_OPENAI_AD_TOKEN` environment variable)
- `azure_ad_token_provider`

An example of using the client with Microsoft Entra ID (formerly known as Azure Active Directory) can be found [here](https://github.com/openai/openai-python/blob/main/examples/azure_ad.py).

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/openai/openai-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import openai
print(openai.__version__)
```

## Requirements

Python 3.8 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).


================================================
File: /api.md
================================================
# Shared Types

```python
from openai.types import (
    ErrorObject,
    FunctionDefinition,
    FunctionParameters,
    ResponseFormatJSONObject,
    ResponseFormatJSONSchema,
    ResponseFormatText,
)
```

# Completions

Types:

```python
from openai.types import Completion, CompletionChoice, CompletionUsage
```

Methods:

- <code title="post /completions">client.completions.<a href="./src/openai/resources/completions.py">create</a>(\*\*<a href="src/openai/types/completion_create_params.py">params</a>) -> <a href="./src/openai/types/completion.py">Completion</a></code>

# Chat

Types:

```python
from openai.types import ChatModel
```

## Completions

Types:

```python
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionAudio,
    ChatCompletionAudioParam,
    ChatCompletionChunk,
    ChatCompletionContentPart,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartInputAudio,
    ChatCompletionContentPartRefusal,
    ChatCompletionContentPartText,
    ChatCompletionDeveloperMessageParam,
    ChatCompletionFunctionCallOption,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionModality,
    ChatCompletionNamedToolChoice,
    ChatCompletionPredictionContent,
    ChatCompletionReasoningEffort,
    ChatCompletionRole,
    ChatCompletionStreamOptions,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionTool,
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/openai/resources/chat/completions.py">create</a>(\*\*<a href="src/openai/types/chat/completion_create_params.py">params</a>) -> <a href="./src/openai/types/chat/chat_completion.py">ChatCompletion</a></code>

# Embeddings

Types:

```python
from openai.types import CreateEmbeddingResponse, Embedding, EmbeddingModel
```

Methods:

- <code title="post /embeddings">client.embeddings.<a href="./src/openai/resources/embeddings.py">create</a>(\*\*<a href="src/openai/types/embedding_create_params.py">params</a>) -> <a href="./src/openai/types/create_embedding_response.py">CreateEmbeddingResponse</a></code>

# Files

Types:

```python
from openai.types import FileContent, FileDeleted, FileObject, FilePurpose
```

Methods:

- <code title="post /files">client.files.<a href="./src/openai/resources/files.py">create</a>(\*\*<a href="src/openai/types/file_create_params.py">params</a>) -> <a href="./src/openai/types/file_object.py">FileObject</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/openai/resources/files.py">retrieve</a>(file_id) -> <a href="./src/openai/types/file_object.py">FileObject</a></code>
- <code title="get /files">client.files.<a href="./src/openai/resources/files.py">list</a>(\*\*<a href="src/openai/types/file_list_params.py">params</a>) -> <a href="./src/openai/types/file_object.py">SyncCursorPage[FileObject]</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/openai/resources/files.py">delete</a>(file_id) -> <a href="./src/openai/types/file_deleted.py">FileDeleted</a></code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/openai/resources/files.py">content</a>(file_id) -> HttpxBinaryResponseContent</code>
- <code title="get /files/{file_id}/content">client.files.<a href="./src/openai/resources/files.py">retrieve_content</a>(file_id) -> str</code>
- <code>client.files.<a href="./src/openai/resources/files.py">wait_for_processing</a>(\*args) -> FileObject</code>

# Images

Types:

```python
from openai.types import Image, ImageModel, ImagesResponse
```

Methods:

- <code title="post /images/variations">client.images.<a href="./src/openai/resources/images.py">create_variation</a>(\*\*<a href="src/openai/types/image_create_variation_params.py">params</a>) -> <a href="./src/openai/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/edits">client.images.<a href="./src/openai/resources/images.py">edit</a>(\*\*<a href="src/openai/types/image_edit_params.py">params</a>) -> <a href="./src/openai/types/images_response.py">ImagesResponse</a></code>
- <code title="post /images/generations">client.images.<a href="./src/openai/resources/images.py">generate</a>(\*\*<a href="src/openai/types/image_generate_params.py">params</a>) -> <a href="./src/openai/types/images_response.py">ImagesResponse</a></code>

# Audio

Types:

```python
from openai.types import AudioModel, AudioResponseFormat
```

## Transcriptions

Types:

```python
from openai.types.audio import (
    Transcription,
    TranscriptionSegment,
    TranscriptionVerbose,
    TranscriptionWord,
    TranscriptionCreateResponse,
)
```

Methods:

- <code title="post /audio/transcriptions">client.audio.transcriptions.<a href="./src/openai/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/openai/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/openai/types/audio/transcription_create_response.py">TranscriptionCreateResponse</a></code>

## Translations

Types:

```python
from openai.types.audio import Translation, TranslationVerbose, TranslationCreateResponse
```

Methods:

- <code title="post /audio/translations">client.audio.translations.<a href="./src/openai/resources/audio/translations.py">create</a>(\*\*<a href="src/openai/types/audio/translation_create_params.py">params</a>) -> <a href="./src/openai/types/audio/translation_create_response.py">TranslationCreateResponse</a></code>

## Speech

Types:

```python
from openai.types.audio import SpeechModel
```

Methods:

- <code title="post /audio/speech">client.audio.speech.<a href="./src/openai/resources/audio/speech.py">create</a>(\*\*<a href="src/openai/types/audio/speech_create_params.py">params</a>) -> HttpxBinaryResponseContent</code>

# Moderations

Types:

```python
from openai.types import (
    Moderation,
    ModerationImageURLInput,
    ModerationModel,
    ModerationMultiModalInput,
    ModerationTextInput,
    ModerationCreateResponse,
)
```

Methods:

- <code title="post /moderations">client.moderations.<a href="./src/openai/resources/moderations.py">create</a>(\*\*<a href="src/openai/types/moderation_create_params.py">params</a>) -> <a href="./src/openai/types/moderation_create_response.py">ModerationCreateResponse</a></code>

# Models

Types:

```python
from openai.types import Model, ModelDeleted
```

Methods:

- <code title="get /models/{model}">client.models.<a href="./src/openai/resources/models.py">retrieve</a>(model) -> <a href="./src/openai/types/model.py">Model</a></code>
- <code title="get /models">client.models.<a href="./src/openai/resources/models.py">list</a>() -> <a href="./src/openai/types/model.py">SyncPage[Model]</a></code>
- <code title="delete /models/{model}">client.models.<a href="./src/openai/resources/models.py">delete</a>(model) -> <a href="./src/openai/types/model_deleted.py">ModelDeleted</a></code>

# FineTuning

## Jobs

Types:

```python
from openai.types.fine_tuning import (
    FineTuningJob,
    FineTuningJobEvent,
    FineTuningJobIntegration,
    FineTuningJobWandbIntegration,
    FineTuningJobWandbIntegrationObject,
)
```

Methods:

- <code title="post /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">create</a>(\*\*<a href="src/openai/types/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">retrieve</a>(fine_tuning_job_id) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">list</a>(\*\*<a href="src/openai/types/fine_tuning/job_list_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">SyncCursorPage[FineTuningJob]</a></code>
- <code title="post /fine_tuning/jobs/{fine_tuning_job_id}/cancel">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">cancel</a>(fine_tuning_job_id) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/events">client.fine_tuning.jobs.<a href="./src/openai/resources/fine_tuning/jobs/jobs.py">list_events</a>(fine_tuning_job_id, \*\*<a href="src/openai/types/fine_tuning/job_list_events_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/fine_tuning_job_event.py">SyncCursorPage[FineTuningJobEvent]</a></code>

### Checkpoints

Types:

```python
from openai.types.fine_tuning.jobs import FineTuningJobCheckpoint
```

Methods:

- <code title="get /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints">client.fine_tuning.jobs.checkpoints.<a href="./src/openai/resources/fine_tuning/jobs/checkpoints.py">list</a>(fine_tuning_job_id, \*\*<a href="src/openai/types/fine_tuning/jobs/checkpoint_list_params.py">params</a>) -> <a href="./src/openai/types/fine_tuning/jobs/fine_tuning_job_checkpoint.py">SyncCursorPage[FineTuningJobCheckpoint]</a></code>

# Beta

## Realtime

Types:

```python
from openai.types.beta.realtime import (
    ConversationCreatedEvent,
    ConversationItem,
    ConversationItemContent,
    ConversationItemCreateEvent,
    ConversationItemCreatedEvent,
    ConversationItemDeleteEvent,
    ConversationItemDeletedEvent,
    ConversationItemInputAudioTranscriptionCompletedEvent,
    ConversationItemInputAudioTranscriptionFailedEvent,
    ConversationItemTruncateEvent,
    ConversationItemTruncatedEvent,
    ErrorEvent,
    InputAudioBufferAppendEvent,
    InputAudioBufferClearEvent,
    InputAudioBufferClearedEvent,
    InputAudioBufferCommitEvent,
    InputAudioBufferCommittedEvent,
    InputAudioBufferSpeechStartedEvent,
    InputAudioBufferSpeechStoppedEvent,
    RateLimitsUpdatedEvent,
    RealtimeClientEvent,
    RealtimeResponse,
    RealtimeResponseStatus,
    RealtimeResponseUsage,
    RealtimeServerEvent,
    ResponseAudioDeltaEvent,
    ResponseAudioDoneEvent,
    ResponseAudioTranscriptDeltaEvent,
    ResponseAudioTranscriptDoneEvent,
    ResponseCancelEvent,
    ResponseContentPartAddedEvent,
    ResponseContentPartDoneEvent,
    ResponseCreateEvent,
    ResponseCreatedEvent,
    ResponseDoneEvent,
    ResponseFunctionCallArgumentsDeltaEvent,
    ResponseFunctionCallArgumentsDoneEvent,
    ResponseOutputItemAddedEvent,
    ResponseOutputItemDoneEvent,
    ResponseTextDeltaEvent,
    ResponseTextDoneEvent,
    SessionCreatedEvent,
    SessionUpdateEvent,
    SessionUpdatedEvent,
)
```

### Sessions

Types:

```python
from openai.types.beta.realtime import Session, SessionCreateResponse
```

Methods:

- <code title="post /realtime/sessions">client.beta.realtime.sessions.<a href="./src/openai/resources/beta/realtime/sessions.py">create</a>(\*\*<a href="src/openai/types/beta/realtime/session_create_params.py">params</a>) -> <a href="./src/openai/types/beta/realtime/session_create_response.py">SessionCreateResponse</a></code>

## VectorStores

Types:

```python
from openai.types.beta import (
    AutoFileChunkingStrategyParam,
    FileChunkingStrategy,
    FileChunkingStrategyParam,
    OtherFileChunkingStrategyObject,
    StaticFileChunkingStrategy,
    StaticFileChunkingStrategyObject,
    StaticFileChunkingStrategyParam,
    VectorStore,
    VectorStoreDeleted,
)
```

Methods:

- <code title="post /vector_stores">client.beta.vector_stores.<a href="./src/openai/resources/beta/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/openai/types/beta/vector_store_create_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_store.py">VectorStore</a></code>
- <code title="get /vector_stores/{vector_store_id}">client.beta.vector_stores.<a href="./src/openai/resources/beta/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/openai/types/beta/vector_store.py">VectorStore</a></code>
- <code title="post /vector_stores/{vector_store_id}">client.beta.vector_stores.<a href="./src/openai/resources/beta/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/openai/types/beta/vector_store_update_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_store.py">VectorStore</a></code>
- <code title="get /vector_stores">client.beta.vector_stores.<a href="./src/openai/resources/beta/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/openai/types/beta/vector_store_list_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_store.py">SyncCursorPage[VectorStore]</a></code>
- <code title="delete /vector_stores/{vector_store_id}">client.beta.vector_stores.<a href="./src/openai/resources/beta/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/openai/types/beta/vector_store_deleted.py">VectorStoreDeleted</a></code>

### Files

Types:

```python
from openai.types.beta.vector_stores import VectorStoreFile, VectorStoreFileDeleted
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/files">client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/openai/types/beta/vector_stores/file_create_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /vector_stores/{vector_store_id}/files/{file_id}">client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /vector_stores/{vector_store_id}/files">client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/openai/types/beta/vector_stores/file_list_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file.py">SyncCursorPage[VectorStoreFile]</a></code>
- <code title="delete /vector_stores/{vector_store_id}/files/{file_id}">client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file_deleted.py">VectorStoreFileDeleted</a></code>
- <code>client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">create_and_poll</a>(\*args) -> VectorStoreFile</code>
- <code>client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">poll</a>(\*args) -> VectorStoreFile</code>
- <code>client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">upload</a>(\*args) -> VectorStoreFile</code>
- <code>client.beta.vector_stores.files.<a href="./src/openai/resources/beta/vector_stores/files.py">upload_and_poll</a>(\*args) -> VectorStoreFile</code>

### FileBatches

Types:

```python
from openai.types.beta.vector_stores import VectorStoreFileBatch
```

Methods:

- <code title="post /vector_stores/{vector_store_id}/file_batches">client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">create</a>(vector_store_id, \*\*<a href="src/openai/types/beta/vector_stores/file_batch_create_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file_batch.py">VectorStoreFileBatch</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}">client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">retrieve</a>(batch_id, \*, vector_store_id) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file_batch.py">VectorStoreFileBatch</a></code>
- <code title="post /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel">client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">cancel</a>(batch_id, \*, vector_store_id) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file_batch.py">VectorStoreFileBatch</a></code>
- <code title="get /vector_stores/{vector_store_id}/file_batches/{batch_id}/files">client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">list_files</a>(batch_id, \*, vector_store_id, \*\*<a href="src/openai/types/beta/vector_stores/file_batch_list_files_params.py">params</a>) -> <a href="./src/openai/types/beta/vector_stores/vector_store_file.py">SyncCursorPage[VectorStoreFile]</a></code>
- <code>client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">create_and_poll</a>(\*args) -> VectorStoreFileBatch</code>
- <code>client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">poll</a>(\*args) -> VectorStoreFileBatch</code>
- <code>client.beta.vector_stores.file_batches.<a href="./src/openai/resources/beta/vector_stores/file_batches.py">upload_and_poll</a>(\*args) -> VectorStoreFileBatch</code>

## Assistants

Types:

```python
from openai.types.beta import (
    Assistant,
    AssistantDeleted,
    AssistantStreamEvent,
    AssistantTool,
    CodeInterpreterTool,
    FileSearchTool,
    FunctionTool,
    MessageStreamEvent,
    RunStepStreamEvent,
    RunStreamEvent,
    ThreadStreamEvent,
)
```

Methods:

- <code title="post /assistants">client.beta.assistants.<a href="./src/openai/resources/beta/assistants.py">create</a>(\*\*<a href="src/openai/types/beta/assistant_create_params.py">params</a>) -> <a href="./src/openai/types/beta/assistant.py">Assistant</a></code>
- <code title="get /assistants/{assistant_id}">client.beta.assistants.<a href="./src/openai/resources/beta/assistants.py">retrieve</a>(assistant_id) -> <a href="./src/openai/types/beta/assistant.py">Assistant</a></code>
- <code title="post /assistants/{assistant_id}">client.beta.assistants.<a href="./src/openai/resources/beta/assistants.py">update</a>(assistant_id, \*\*<a href="src/openai/types/beta/assistant_update_params.py">params</a>) -> <a href="./src/openai/types/beta/assistant.py">Assistant</a></code>
- <code title="get /assistants">client.beta.assistants.<a href="./src/openai/resources/beta/assistants.py">list</a>(\*\*<a href="src/openai/types/beta/assistant_list_params.py">params</a>) -> <a href="./src/openai/types/beta/assistant.py">SyncCursorPage[Assistant]</a></code>
- <code title="delete /assistants/{assistant_id}">client.beta.assistants.<a href="./src/openai/resources/beta/assistants.py">delete</a>(assistant_id) -> <a href="./src/openai/types/beta/assistant_deleted.py">AssistantDeleted</a></code>

## Threads

Types:

```python
from openai.types.beta import (
    AssistantResponseFormatOption,
    AssistantToolChoice,
    AssistantToolChoiceFunction,
    AssistantToolChoiceOption,
    Thread,
    ThreadDeleted,
)
```

Methods:

- <code title="post /threads">client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">create</a>(\*\*<a href="src/openai/types/beta/thread_create_params.py">params</a>) -> <a href="./src/openai/types/beta/thread.py">Thread</a></code>
- <code title="get /threads/{thread_id}">client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">retrieve</a>(thread_id) -> <a href="./src/openai/types/beta/thread.py">Thread</a></code>
- <code title="post /threads/{thread_id}">client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">update</a>(thread_id, \*\*<a href="src/openai/types/beta/thread_update_params.py">params</a>) -> <a href="./src/openai/types/beta/thread.py">Thread</a></code>
- <code title="delete /threads/{thread_id}">client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">delete</a>(thread_id) -> <a href="./src/openai/types/beta/thread_deleted.py">ThreadDeleted</a></code>
- <code title="post /threads/runs">client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">create_and_run</a>(\*\*<a href="src/openai/types/beta/thread_create_and_run_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/run.py">Run</a></code>
- <code>client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">create_and_run_poll</a>(\*args) -> Run</code>
- <code>client.beta.threads.<a href="./src/openai/resources/beta/threads/threads.py">create_and_run_stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>

### Runs

Types:

```python
from openai.types.beta.threads import RequiredActionFunctionToolCall, Run, RunStatus
```

Methods:

- <code title="post /threads/{thread_id}/runs">client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">create</a>(thread_id, \*\*<a href="src/openai/types/beta/threads/run_create_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/run.py">Run</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}">client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">retrieve</a>(run_id, \*, thread_id) -> <a href="./src/openai/types/beta/threads/run.py">Run</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}">client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">update</a>(run_id, \*, thread_id, \*\*<a href="src/openai/types/beta/threads/run_update_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/run.py">Run</a></code>
- <code title="get /threads/{thread_id}/runs">client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">list</a>(thread_id, \*\*<a href="src/openai/types/beta/threads/run_list_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/run.py">SyncCursorPage[Run]</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/cancel">client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">cancel</a>(run_id, \*, thread_id) -> <a href="./src/openai/types/beta/threads/run.py">Run</a></code>
- <code title="post /threads/{thread_id}/runs/{run_id}/submit_tool_outputs">client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">submit_tool_outputs</a>(run_id, \*, thread_id, \*\*<a href="src/openai/types/beta/threads/run_submit_tool_outputs_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/run.py">Run</a></code>
- <code>client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">create_and_poll</a>(\*args) -> Run</code>
- <code>client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">create_and_stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>
- <code>client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">poll</a>(\*args) -> Run</code>
- <code>client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>
- <code>client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">submit_tool_outputs_and_poll</a>(\*args) -> Run</code>
- <code>client.beta.threads.runs.<a href="./src/openai/resources/beta/threads/runs/runs.py">submit_tool_outputs_stream</a>(\*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]</code>

#### Steps

Types:

```python
from openai.types.beta.threads.runs import (
    CodeInterpreterLogs,
    CodeInterpreterOutputImage,
    CodeInterpreterToolCall,
    CodeInterpreterToolCallDelta,
    FileSearchToolCall,
    FileSearchToolCallDelta,
    FunctionToolCall,
    FunctionToolCallDelta,
    MessageCreationStepDetails,
    RunStep,
    RunStepDelta,
    RunStepDeltaEvent,
    RunStepDeltaMessageDelta,
    RunStepInclude,
    ToolCall,
    ToolCallDelta,
    ToolCallDeltaObject,
    ToolCallsStepDetails,
)
```

Methods:

- <code title="get /threads/{thread_id}/runs/{run_id}/steps/{step_id}">client.beta.threads.runs.steps.<a href="./src/openai/resources/beta/threads/runs/steps.py">retrieve</a>(step_id, \*, thread_id, run_id, \*\*<a href="src/openai/types/beta/threads/runs/step_retrieve_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/runs/run_step.py">RunStep</a></code>
- <code title="get /threads/{thread_id}/runs/{run_id}/steps">client.beta.threads.runs.steps.<a href="./src/openai/resources/beta/threads/runs/steps.py">list</a>(run_id, \*, thread_id, \*\*<a href="src/openai/types/beta/threads/runs/step_list_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/runs/run_step.py">SyncCursorPage[RunStep]</a></code>

### Messages

Types:

```python
from openai.types.beta.threads import (
    Annotation,
    AnnotationDelta,
    FileCitationAnnotation,
    FileCitationDeltaAnnotation,
    FilePathAnnotation,
    FilePathDeltaAnnotation,
    ImageFile,
    ImageFileContentBlock,
    ImageFileDelta,
    ImageFileDeltaBlock,
    ImageURL,
    ImageURLContentBlock,
    ImageURLDelta,
    ImageURLDeltaBlock,
    Message,
    MessageContent,
    MessageContentDelta,
    MessageContentPartParam,
    MessageDeleted,
    MessageDelta,
    MessageDeltaEvent,
    RefusalContentBlock,
    RefusalDeltaBlock,
    Text,
    TextContentBlock,
    TextContentBlockParam,
    TextDelta,
    TextDeltaBlock,
)
```

Methods:

- <code title="post /threads/{thread_id}/messages">client.beta.threads.messages.<a href="./src/openai/resources/beta/threads/messages.py">create</a>(thread_id, \*\*<a href="src/openai/types/beta/threads/message_create_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/message.py">Message</a></code>
- <code title="get /threads/{thread_id}/messages/{message_id}">client.beta.threads.messages.<a href="./src/openai/resources/beta/threads/messages.py">retrieve</a>(message_id, \*, thread_id) -> <a href="./src/openai/types/beta/threads/message.py">Message</a></code>
- <code title="post /threads/{thread_id}/messages/{message_id}">client.beta.threads.messages.<a href="./src/openai/resources/beta/threads/messages.py">update</a>(message_id, \*, thread_id, \*\*<a href="src/openai/types/beta/threads/message_update_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/message.py">Message</a></code>
- <code title="get /threads/{thread_id}/messages">client.beta.threads.messages.<a href="./src/openai/resources/beta/threads/messages.py">list</a>(thread_id, \*\*<a href="src/openai/types/beta/threads/message_list_params.py">params</a>) -> <a href="./src/openai/types/beta/threads/message.py">SyncCursorPage[Message]</a></code>
- <code title="delete /threads/{thread_id}/messages/{message_id}">client.beta.threads.messages.<a href="./src/openai/resources/beta/threads/messages.py">delete</a>(message_id, \*, thread_id) -> <a href="./src/openai/types/beta/threads/message_deleted.py">MessageDeleted</a></code>

# Batches

Types:

```python
from openai.types import Batch, BatchError, BatchRequestCounts
```

Methods:

- <code title="post /batches">client.batches.<a href="./src/openai/resources/batches.py">create</a>(\*\*<a href="src/openai/types/batch_create_params.py">params</a>) -> <a href="./src/openai/types/batch.py">Batch</a></code>
- <code title="get /batches/{batch_id}">client.batches.<a href="./src/openai/resources/batches.py">retrieve</a>(batch_id) -> <a href="./src/openai/types/batch.py">Batch</a></code>
- <code title="get /batches">client.batches.<a href="./src/openai/resources/batches.py">list</a>(\*\*<a href="src/openai/types/batch_list_params.py">params</a>) -> <a href="./src/openai/types/batch.py">SyncCursorPage[Batch]</a></code>
- <code title="post /batches/{batch_id}/cancel">client.batches.<a href="./src/openai/resources/batches.py">cancel</a>(batch_id) -> <a href="./src/openai/types/batch.py">Batch</a></code>

# Uploads

Types:

```python
from openai.types import Upload
```

Methods:

- <code title="post /uploads">client.uploads.<a href="./src/openai/resources/uploads/uploads.py">create</a>(\*\*<a href="src/openai/types/upload_create_params.py">params</a>) -> <a href="./src/openai/types/upload.py">Upload</a></code>
- <code title="post /uploads/{upload_id}/cancel">client.uploads.<a href="./src/openai/resources/uploads/uploads.py">cancel</a>(upload_id) -> <a href="./src/openai/types/upload.py">Upload</a></code>
- <code title="post /uploads/{upload_id}/complete">client.uploads.<a href="./src/openai/resources/uploads/uploads.py">complete</a>(upload_id, \*\*<a href="src/openai/types/upload_complete_params.py">params</a>) -> <a href="./src/openai/types/upload.py">Upload</a></code>

## Parts

Types:

```python
from openai.types.uploads import UploadPart
```

Methods:

- <code title="post /uploads/{upload_id}/parts">client.uploads.parts.<a href="./src/openai/resources/uploads/parts.py">create</a>(upload_id, \*\*<a href="src/openai/types/uploads/part_create_params.py">params</a>) -> <a href="./src/openai/types/uploads/upload_part.py">UploadPart</a></code>


================================================
File: /tests/sample_file.txt
================================================
Hello, world!


================================================
File: /tests/api_resources/test_completions.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import Completion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: OpenAI) -> None:
        completion = client.completions.create(
            model="string",
            prompt="This is a test.",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: OpenAI) -> None:
        completion = client.completions.create(
            model="string",
            prompt="This is a test.",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=-9007199254740991,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: OpenAI) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: OpenAI) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: OpenAI) -> None:
        completion_stream = client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: OpenAI) -> None:
        completion_stream = client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=-9007199254740991,
            stop="\n",
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: OpenAI) -> None:
        response = client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: OpenAI) -> None:
        with client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        completion = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=-9007199254740991,
            stop="\n",
            stream=False,
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        completion_stream = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncOpenAI) -> None:
        completion_stream = await async_client.completions.create(
            model="string",
            prompt="This is a test.",
            stream=True,
            best_of=0,
            echo=True,
            frequency_penalty=-2,
            logit_bias={"foo": 0},
            logprobs=0,
            max_tokens=16,
            n=1,
            presence_penalty=-2,
            seed=-9007199254740991,
            stop="\n",
            stream_options={"include_usage": True},
            suffix="test.",
            temperature=1,
            top_p=1,
            user="user-1234",
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="string",
            prompt="This is a test.",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/audio/test_transcriptions.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types.audio import TranscriptionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        transcription = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        transcription = client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
            language="string",
            prompt="string",
            response_format="json",
            temperature=0,
            timestamp_granularities=["word"],
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="whisper-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.audio.transcriptions.with_streaming_response.create(
            file=b"raw file contents",
            model="whisper-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        transcription = await async_client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        transcription = await async_client.audio.transcriptions.create(
            file=b"raw file contents",
            model="whisper-1",
            language="string",
            prompt="string",
            response_format="json",
            temperature=0,
            timestamp_granularities=["word"],
        )
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.create(
            file=b"raw file contents",
            model="whisper-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.create(
            file=b"raw file contents",
            model="whisper-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(TranscriptionCreateResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/audio/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/audio/test_speech.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

import openai._legacy_response as _legacy_response
from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.audio.speech.create(
            input="string",
            model="string",
            voice="alloy",
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)
        assert speech.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = client.audio.speech.create(
            input="string",
            model="string",
            voice="alloy",
            response_format="mp3",
            speed=0.25,
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)
        assert speech.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = client.audio.speech.with_raw_response.create(
            input="string",
            model="string",
            voice="alloy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = response.parse()
        assert_matches_type(_legacy_response.HttpxBinaryResponseContent, speech, path=["response"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.audio.speech.with_streaming_response.create(
            input="string",
            model="string",
            voice="alloy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = response.parse()
            assert_matches_type(bytes, speech, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeech:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.audio.speech.create(
            input="string",
            model="string",
            voice="alloy",
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)
        assert speech.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        speech = await async_client.audio.speech.create(
            input="string",
            model="string",
            voice="alloy",
            response_format="mp3",
            speed=0.25,
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)
        assert speech.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = await async_client.audio.speech.with_raw_response.create(
            input="string",
            model="string",
            voice="alloy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speech = response.parse()
        assert_matches_type(_legacy_response.HttpxBinaryResponseContent, speech, path=["response"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.post("/audio/speech").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.audio.speech.with_streaming_response.create(
            input="string",
            model="string",
            voice="alloy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speech = await response.parse()
            assert_matches_type(bytes, speech, path=["response"])

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/audio/test_translations.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types.audio import TranslationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranslations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        translation = client.audio.translations.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(TranslationCreateResponse, translation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        translation = client.audio.translations.create(
            file=b"raw file contents",
            model="whisper-1",
            prompt="prompt",
            response_format="json",
            temperature=0,
        )
        assert_matches_type(TranslationCreateResponse, translation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.audio.translations.with_raw_response.create(
            file=b"raw file contents",
            model="whisper-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationCreateResponse, translation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.audio.translations.with_streaming_response.create(
            file=b"raw file contents",
            model="whisper-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(TranslationCreateResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranslations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        translation = await async_client.audio.translations.create(
            file=b"raw file contents",
            model="whisper-1",
        )
        assert_matches_type(TranslationCreateResponse, translation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        translation = await async_client.audio.translations.create(
            file=b"raw file contents",
            model="whisper-1",
            prompt="prompt",
            response_format="json",
            temperature=0,
        )
        assert_matches_type(TranslationCreateResponse, translation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.audio.translations.with_raw_response.create(
            file=b"raw file contents",
            model="whisper-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationCreateResponse, translation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.audio.translations.with_streaming_response.create(
            file=b"raw file contents",
            model="whisper-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(TranslationCreateResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/test_moderations.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import ModerationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        moderation = client.moderations.create(
            input="I want to kill them.",
        )
        assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        moderation = client.moderations.create(
            input="I want to kill them.",
            model="omni-moderation-2024-09-26",
        )
        assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.moderations.with_raw_response.create(
            input="I want to kill them.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.moderations.with_streaming_response.create(
            input="I want to kill them.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = response.parse()
            assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        moderation = await async_client.moderations.create(
            input="I want to kill them.",
        )
        assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        moderation = await async_client.moderations.create(
            input="I want to kill them.",
            model="omni-moderation-2024-09-26",
        )
        assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.moderations.with_raw_response.create(
            input="I want to kill them.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        moderation = response.parse()
        assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.moderations.with_streaming_response.create(
            input="I want to kill them.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            moderation = await response.parse()
            assert_matches_type(ModerationCreateResponse, moderation, path=["response"])

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/test_images.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import ImagesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_variation(self, client: OpenAI) -> None:
        image = client.images.create_variation(
            image=b"raw file contents",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_method_create_variation_with_all_params(self, client: OpenAI) -> None:
        image = client.images.create_variation(
            image=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="256x256",
            user="user-1234",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_raw_response_create_variation(self, client: OpenAI) -> None:
        response = client.images.with_raw_response.create_variation(
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_streaming_response_create_variation(self, client: OpenAI) -> None:
        with client.images.with_streaming_response.create_variation(
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImagesResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edit(self, client: OpenAI) -> None:
        image = client.images.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: OpenAI) -> None:
        image = client.images.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
            mask=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="256x256",
            user="user-1234",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: OpenAI) -> None:
        response = client.images.with_raw_response.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: OpenAI) -> None:
        with client.images.with_streaming_response.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImagesResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate(self, client: OpenAI) -> None:
        image = client.images.generate(
            prompt="A cute baby sea otter",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_method_generate_with_all_params(self, client: OpenAI) -> None:
        image = client.images.generate(
            prompt="A cute baby sea otter",
            model="dall-e-3",
            n=1,
            quality="standard",
            response_format="url",
            size="256x256",
            style="vivid",
            user="user-1234",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_raw_response_generate(self, client: OpenAI) -> None:
        response = client.images.with_raw_response.generate(
            prompt="A cute baby sea otter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    def test_streaming_response_generate(self, client: OpenAI) -> None:
        with client.images.with_streaming_response.generate(
            prompt="A cute baby sea otter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(ImagesResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_variation(self, async_client: AsyncOpenAI) -> None:
        image = await async_client.images.create_variation(
            image=b"raw file contents",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_method_create_variation_with_all_params(self, async_client: AsyncOpenAI) -> None:
        image = await async_client.images.create_variation(
            image=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="256x256",
            user="user-1234",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_raw_response_create_variation(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.images.with_raw_response.create_variation(
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_streaming_response_create_variation(self, async_client: AsyncOpenAI) -> None:
        async with async_client.images.with_streaming_response.create_variation(
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImagesResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edit(self, async_client: AsyncOpenAI) -> None:
        image = await async_client.images.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncOpenAI) -> None:
        image = await async_client.images.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
            mask=b"raw file contents",
            model="dall-e-2",
            n=1,
            response_format="url",
            size="256x256",
            user="user-1234",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.images.with_raw_response.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncOpenAI) -> None:
        async with async_client.images.with_streaming_response.edit(
            image=b"raw file contents",
            prompt="A cute baby sea otter wearing a beret",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImagesResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate(self, async_client: AsyncOpenAI) -> None:
        image = await async_client.images.generate(
            prompt="A cute baby sea otter",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_method_generate_with_all_params(self, async_client: AsyncOpenAI) -> None:
        image = await async_client.images.generate(
            prompt="A cute baby sea otter",
            model="dall-e-3",
            n=1,
            quality="standard",
            response_format="url",
            size="256x256",
            style="vivid",
            user="user-1234",
        )
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.images.with_raw_response.generate(
            prompt="A cute baby sea otter",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(ImagesResponse, image, path=["response"])

    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncOpenAI) -> None:
        async with async_client.images.with_streaming_response.generate(
            prompt="A cute baby sea otter",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(ImagesResponse, image, path=["response"])

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/test_batches.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import Batch
from openai.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        batch = client.batches.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        batch = client.batches.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
            metadata={"foo": "string"},
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.batches.with_raw_response.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.batches.with_streaming_response.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(Batch, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        batch = client.batches.retrieve(
            "string",
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.batches.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.batches.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(Batch, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        batch = client.batches.list()
        assert_matches_type(SyncCursorPage[Batch], batch, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        batch = client.batches.list(
            after="string",
            limit=0,
        )
        assert_matches_type(SyncCursorPage[Batch], batch, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(SyncCursorPage[Batch], batch, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(SyncCursorPage[Batch], batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: OpenAI) -> None:
        batch = client.batches.cancel(
            "string",
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: OpenAI) -> None:
        response = client.batches.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: OpenAI) -> None:
        with client.batches.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(Batch, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.cancel(
                "",
            )


class TestAsyncBatches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        batch = await async_client.batches.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        batch = await async_client.batches.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
            metadata={"foo": "string"},
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.batches.with_raw_response.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.batches.with_streaming_response.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(Batch, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        batch = await async_client.batches.retrieve(
            "string",
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.batches.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.batches.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(Batch, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        batch = await async_client.batches.list()
        assert_matches_type(AsyncCursorPage[Batch], batch, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        batch = await async_client.batches.list(
            after="string",
            limit=0,
        )
        assert_matches_type(AsyncCursorPage[Batch], batch, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(AsyncCursorPage[Batch], batch, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(AsyncCursorPage[Batch], batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpenAI) -> None:
        batch = await async_client.batches.cancel(
            "string",
        )
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.batches.with_raw_response.cancel(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(Batch, batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpenAI) -> None:
        async with async_client.batches.with_streaming_response.cancel(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(Batch, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.cancel(
                "",
            )


================================================
File: /tests/api_resources/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/test_files.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

import openai._legacy_response as _legacy_response
from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import FileObject, FileDeleted
from openai.pagination import SyncCursorPage, AsyncCursorPage

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        file = client.files.create(
            file=b"raw file contents",
            purpose="assistants",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.create(
            file=b"raw file contents",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.create(
            file=b"raw file contents",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        file = client.files.retrieve(
            "string",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        file = client.files.list()
        assert_matches_type(SyncCursorPage[FileObject], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        file = client.files.list(
            after="after",
            limit=0,
            order="asc",
            purpose="purpose",
        )
        assert_matches_type(SyncCursorPage[FileObject], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncCursorPage[FileObject], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncCursorPage[FileObject], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        file = client.files.delete(
            "string",
        )
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.files.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.files.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_content(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = client.files.content(
            "string",
        )
        assert isinstance(file, _legacy_response.HttpxBinaryResponseContent)
        assert file.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_content(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = client.files.with_raw_response.content(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(_legacy_response.HttpxBinaryResponseContent, file, path=["response"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_content(self, client: OpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.files.with_streaming_response.content(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(bytes, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_content(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.content(
                "",
            )

    @parametrize
    def test_method_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            file = client.files.retrieve_content(
                "string",
            )

        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.files.with_raw_response.retrieve_content(
                "string",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            with client.files.with_streaming_response.retrieve_content(
                "string",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = response.parse()
                assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_content(self, client: OpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.files.with_raw_response.retrieve_content(
                    "",
                )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.files.create(
            file=b"raw file contents",
            purpose="assistants",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.files.with_raw_response.create(
            file=b"raw file contents",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.files.with_streaming_response.create(
            file=b"raw file contents",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.files.retrieve(
            "string",
        )
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.files.list()
        assert_matches_type(AsyncCursorPage[FileObject], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.files.list(
            after="after",
            limit=0,
            order="asc",
            purpose="purpose",
        )
        assert_matches_type(AsyncCursorPage[FileObject], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(AsyncCursorPage[FileObject], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncCursorPage[FileObject], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.files.delete(
            "string",
        )
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.files.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleted, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.files.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_content(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = await async_client.files.content(
            "string",
        )
        assert isinstance(file, _legacy_response.HttpxBinaryResponseContent)
        assert file.json() == {"foo": "bar"}

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_content(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = await async_client.files.with_raw_response.content(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(_legacy_response.HttpxBinaryResponseContent, file, path=["response"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_content(self, async_client: AsyncOpenAI, respx_mock: MockRouter) -> None:
        respx_mock.get("/files/string/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.files.with_streaming_response.content(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(bytes, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_content(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.content(
                "",
            )

    @parametrize
    async def test_method_retrieve_content(self, async_client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            file = await async_client.files.retrieve_content(
                "string",
            )

        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_content(self, async_client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.files.with_raw_response.retrieve_content(
                "string",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(str, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_content(self, async_client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.files.with_streaming_response.retrieve_content(
                "string",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                file = await response.parse()
                assert_matches_type(str, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_content(self, async_client: AsyncOpenAI) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.files.with_raw_response.retrieve_content(
                    "",
                )


================================================
File: /tests/api_resources/uploads/test_parts.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types.uploads import UploadPart

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        part = client.uploads.parts.create(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )
        assert_matches_type(UploadPart, part, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.uploads.parts.with_raw_response.create(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(UploadPart, part, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.uploads.parts.with_streaming_response.create(
            upload_id="upload_abc123",
            data=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(UploadPart, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.parts.with_raw_response.create(
                upload_id="",
                data=b"raw file contents",
            )


class TestAsyncParts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        part = await async_client.uploads.parts.create(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )
        assert_matches_type(UploadPart, part, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.uploads.parts.with_raw_response.create(
            upload_id="upload_abc123",
            data=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(UploadPart, part, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.uploads.parts.with_streaming_response.create(
            upload_id="upload_abc123",
            data=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(UploadPart, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.parts.with_raw_response.create(
                upload_id="",
                data=b"raw file contents",
            )


================================================
File: /tests/api_resources/uploads/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/test_uploads.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import Upload

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        upload = client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.uploads.with_raw_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.uploads.with_streaming_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: OpenAI) -> None:
        upload = client.uploads.cancel(
            "upload_abc123",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: OpenAI) -> None:
        response = client.uploads.with_raw_response.cancel(
            "upload_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: OpenAI) -> None:
        with client.uploads.with_streaming_response.cancel(
            "upload_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_complete(self, client: OpenAI) -> None:
        upload = client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_method_complete_with_all_params(self, client: OpenAI) -> None:
        upload = client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
            md5="md5",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: OpenAI) -> None:
        response = client.uploads.with_raw_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: OpenAI) -> None:
        with client.uploads.with_streaming_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.uploads.with_raw_response.complete(
                upload_id="",
                part_ids=["string"],
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        upload = await async_client.uploads.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.uploads.with_raw_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.uploads.with_streaming_response.create(
            bytes=0,
            filename="filename",
            mime_type="mime_type",
            purpose="assistants",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpenAI) -> None:
        upload = await async_client.uploads.cancel(
            "upload_abc123",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.uploads.with_raw_response.cancel(
            "upload_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpenAI) -> None:
        async with async_client.uploads.with_streaming_response.cancel(
            "upload_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_complete(self, async_client: AsyncOpenAI) -> None:
        upload = await async_client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncOpenAI) -> None:
        upload = await async_client.uploads.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
            md5="md5",
        )
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.uploads.with_raw_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(Upload, upload, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.uploads.with_streaming_response.complete(
            upload_id="upload_abc123",
            part_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(Upload, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.uploads.with_raw_response.complete(
                upload_id="",
                part_ids=["string"],
            )


================================================
File: /tests/api_resources/test_models.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types import Model, ModelDeleted
from openai.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        model = client.models.retrieve(
            "gpt-4o-mini",
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.models.with_raw_response.retrieve(
            "gpt-4o-mini",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.models.with_streaming_response.retrieve(
            "gpt-4o-mini",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        model = client.models.list()
        assert_matches_type(SyncPage[Model], model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(SyncPage[Model], model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(SyncPage[Model], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        model = client.models.delete(
            "ft:gpt-4o-mini:acemeco:suffix:abc123",
        )
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.models.with_raw_response.delete(
            "ft:gpt-4o-mini:acemeco:suffix:abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.models.with_streaming_response.delete(
            "ft:gpt-4o-mini:acemeco:suffix:abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelDeleted, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            client.models.with_raw_response.delete(
                "",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        model = await async_client.models.retrieve(
            "gpt-4o-mini",
        )
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            "gpt-4o-mini",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(Model, model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            "gpt-4o-mini",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(Model, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        model = await async_client.models.list()
        assert_matches_type(AsyncPage[Model], model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(AsyncPage[Model], model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(AsyncPage[Model], model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenAI) -> None:
        model = await async_client.models.delete(
            "ft:gpt-4o-mini:acemeco:suffix:abc123",
        )
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.models.with_raw_response.delete(
            "ft:gpt-4o-mini:acemeco:suffix:abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDeleted, model, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.models.with_streaming_response.delete(
            "ft:gpt-4o-mini:acemeco:suffix:abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelDeleted, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model` but received ''"):
            await async_client.models.with_raw_response.delete(
                "",
            )


================================================
File: /tests/api_resources/beta/threads/runs/test_steps.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta.threads.runs import RunStep

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        step = client.beta.threads.runs.steps.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpenAI) -> None:
        step = client.beta.threads.runs.steps.retrieve(
            step_id="step_id",
            thread_id="thread_id",
            run_id="run_id",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
        )
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.steps.with_raw_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.threads.runs.steps.with_streaming_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(RunStep, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="",
                run_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="string",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.retrieve(
                "",
                thread_id="string",
                run_id="string",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        step = client.beta.threads.runs.steps.list(
            "string",
            thread_id="string",
        )
        assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        step = client.beta.threads.runs.steps.list(
            run_id="run_id",
            thread_id="thread_id",
            after="after",
            before="before",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.steps.with_raw_response.list(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.beta.threads.runs.steps.with_streaming_response.list(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(SyncCursorPage[RunStep], step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.list(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.steps.with_raw_response.list(
                "",
                thread_id="string",
            )


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        step = await async_client.beta.threads.runs.steps.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpenAI) -> None:
        step = await async_client.beta.threads.runs.steps.retrieve(
            step_id="step_id",
            thread_id="thread_id",
            run_id="run_id",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
        )
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(RunStep, step, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.steps.with_streaming_response.retrieve(
            "string",
            thread_id="string",
            run_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(RunStep, step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="",
                run_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
                "string",
                thread_id="string",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.retrieve(
                "",
                thread_id="string",
                run_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        step = await async_client.beta.threads.runs.steps.list(
            "string",
            thread_id="string",
        )
        assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        step = await async_client.beta.threads.runs.steps.list(
            run_id="run_id",
            thread_id="thread_id",
            after="after",
            before="before",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.steps.with_raw_response.list(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.steps.with_streaming_response.list(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(AsyncCursorPage[RunStep], step, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.list(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.steps.with_raw_response.list(
                "",
                thread_id="string",
            )


================================================
File: /tests/api_resources/beta/threads/runs/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/beta/threads/test_messages.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta.threads import (
    Message,
    MessageDeleted,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.create(
            "string",
            content="string",
            role="user",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.create(
            "string",
            content="string",
            role="user",
            attachments=[
                {
                    "file_id": "file_id",
                    "tools": [{"type": "code_interpreter"}],
                }
            ],
            metadata={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.threads.messages.with_raw_response.create(
            "string",
            content="string",
            role="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.threads.messages.with_streaming_response.create(
            "string",
            content="string",
            role="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.messages.with_raw_response.create(
                "",
                content="string",
                role="user",
            )

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.retrieve(
            "string",
            thread_id="string",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.threads.messages.with_raw_response.retrieve(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.threads.messages.with_streaming_response.retrieve(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.messages.with_raw_response.retrieve(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.beta.threads.messages.with_raw_response.retrieve(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_update(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.update(
            "string",
            thread_id="string",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.update(
            "string",
            thread_id="string",
            metadata={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: OpenAI) -> None:
        response = client.beta.threads.messages.with_raw_response.update(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: OpenAI) -> None:
        with client.beta.threads.messages.with_streaming_response.update(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.messages.with_raw_response.update(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.beta.threads.messages.with_raw_response.update(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.list(
            "string",
        )
        assert_matches_type(SyncCursorPage[Message], message, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.list(
            "string",
            after="string",
            before="string",
            limit=0,
            order="asc",
            run_id="string",
        )
        assert_matches_type(SyncCursorPage[Message], message, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.beta.threads.messages.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncCursorPage[Message], message, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.beta.threads.messages.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncCursorPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.messages.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        message = client.beta.threads.messages.delete(
            "string",
            thread_id="string",
        )
        assert_matches_type(MessageDeleted, message, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.beta.threads.messages.with_raw_response.delete(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleted, message, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.beta.threads.messages.with_streaming_response.delete(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageDeleted, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.messages.with_raw_response.delete(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.beta.threads.messages.with_raw_response.delete(
                "",
                thread_id="string",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.create(
            "string",
            content="string",
            role="user",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.create(
            "string",
            content="string",
            role="user",
            attachments=[
                {
                    "file_id": "file_id",
                    "tools": [{"type": "code_interpreter"}],
                }
            ],
            metadata={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.messages.with_raw_response.create(
            "string",
            content="string",
            role="user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.messages.with_streaming_response.create(
            "string",
            content="string",
            role="user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.create(
                "",
                content="string",
                role="user",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.retrieve(
            "string",
            thread_id="string",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.messages.with_raw_response.retrieve(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.messages.with_streaming_response.retrieve(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.retrieve(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.retrieve(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.update(
            "string",
            thread_id="string",
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.update(
            "string",
            thread_id="string",
            metadata={},
        )
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.messages.with_raw_response.update(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(Message, message, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.messages.with_streaming_response.update(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(Message, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.update(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.update(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.list(
            "string",
        )
        assert_matches_type(AsyncCursorPage[Message], message, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.list(
            "string",
            after="string",
            before="string",
            limit=0,
            order="asc",
            run_id="string",
        )
        assert_matches_type(AsyncCursorPage[Message], message, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.messages.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(AsyncCursorPage[Message], message, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.messages.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncCursorPage[Message], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenAI) -> None:
        message = await async_client.beta.threads.messages.delete(
            "string",
            thread_id="string",
        )
        assert_matches_type(MessageDeleted, message, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.messages.with_raw_response.delete(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleted, message, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.messages.with_streaming_response.delete(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageDeleted, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.delete(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.beta.threads.messages.with_raw_response.delete(
                "",
                thread_id="string",
            )


================================================
File: /tests/api_resources/beta/threads/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/beta/threads/test_runs.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta.threads import (
    Run,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.create(
            "string",
            assistant_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.create(
            thread_id="thread_id",
            assistant_id="assistant_id",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            additional_instructions="additional_instructions",
            additional_messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {},
                }
            ],
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.create(
            "string",
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.create(
            "string",
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.create(
                "",
                assistant_id="string",
            )

    @parametrize
    def test_method_create_overload_2(self, client: OpenAI) -> None:
        run_stream = client.beta.threads.runs.create(
            "string",
            assistant_id="string",
            stream=True,
        )
        run_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: OpenAI) -> None:
        run_stream = client.beta.threads.runs.create(
            "string",
            assistant_id="string",
            stream=True,
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            additional_instructions="additional_instructions",
            additional_messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {},
                }
            ],
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            temperature=1,
            tool_choice="none",
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        run_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.create(
            "string",
            assistant_id="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.create(
            "string",
            assistant_id="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.create(
                "",
                assistant_id="string",
                stream=True,
            )

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.retrieve(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.retrieve(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.retrieve(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.retrieve(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.retrieve(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_update(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.update(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.update(
            "string",
            thread_id="string",
            metadata={},
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.update(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.update(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.update(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.update(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.list(
            "string",
        )
        assert_matches_type(SyncCursorPage[Run], run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.list(
            "string",
            after="string",
            before="string",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[Run], run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncCursorPage[Run], run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncCursorPage[Run], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.cancel(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.cancel(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.cancel(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.cancel(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.cancel(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_submit_tool_outputs_overload_1(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_method_submit_tool_outputs_with_all_params_overload_1(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[
                {
                    "output": "output",
                    "tool_call_id": "tool_call_id",
                }
            ],
            stream=False,
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_submit_tool_outputs_overload_1(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_submit_tool_outputs_overload_1(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_tool_outputs_overload_1(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "string",
                thread_id="",
                tool_outputs=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                run_id="",
                thread_id="thread_id",
                tool_outputs=[{}],
            )

    @parametrize
    def test_method_submit_tool_outputs_overload_2(self, client: OpenAI) -> None:
        run_stream = client.beta.threads.runs.submit_tool_outputs(
            "string",
            thread_id="string",
            stream=True,
            tool_outputs=[{}],
        )
        run_stream.response.close()

    @parametrize
    def test_raw_response_submit_tool_outputs_overload_2(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.submit_tool_outputs(
            "string",
            thread_id="string",
            stream=True,
            tool_outputs=[{}],
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_submit_tool_outputs_overload_2(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.submit_tool_outputs(
            "string",
            thread_id="string",
            stream=True,
            tool_outputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_tool_outputs_overload_2(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "string",
                thread_id="",
                stream=True,
                tool_outputs=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "",
                thread_id="string",
                stream=True,
                tool_outputs=[{}],
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.create(
            "string",
            assistant_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.create(
            thread_id="thread_id",
            assistant_id="assistant_id",
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            additional_instructions="additional_instructions",
            additional_messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {},
                }
            ],
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.create(
            "string",
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.create(
            "string",
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.create(
                "",
                assistant_id="string",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        run_stream = await async_client.beta.threads.runs.create(
            "string",
            assistant_id="string",
            stream=True,
        )
        await run_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncOpenAI) -> None:
        run_stream = await async_client.beta.threads.runs.create(
            "string",
            assistant_id="string",
            stream=True,
            include=["step_details.tool_calls[*].file_search.results[*].content"],
            additional_instructions="additional_instructions",
            additional_messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {},
                }
            ],
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            temperature=1,
            tool_choice="none",
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        await run_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.create(
            "string",
            assistant_id="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.create(
            "string",
            assistant_id="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.create(
                "",
                assistant_id="string",
                stream=True,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.retrieve(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.retrieve(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.retrieve(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.retrieve(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.retrieve(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.update(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.update(
            "string",
            thread_id="string",
            metadata={},
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.update(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.update(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.update(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.update(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.list(
            "string",
        )
        assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.list(
            "string",
            after="string",
            before="string",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.cancel(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.cancel(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.cancel(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.cancel(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.cancel(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_submit_tool_outputs_overload_1(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_method_submit_tool_outputs_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[
                {
                    "output": "output",
                    "tool_call_id": "tool_call_id",
                }
            ],
            stream=False,
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_submit_tool_outputs_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_submit_tool_outputs_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.submit_tool_outputs(
            run_id="run_id",
            thread_id="thread_id",
            tool_outputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_tool_outputs_overload_1(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "string",
                thread_id="",
                tool_outputs=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                run_id="",
                thread_id="thread_id",
                tool_outputs=[{}],
            )

    @parametrize
    async def test_method_submit_tool_outputs_overload_2(self, async_client: AsyncOpenAI) -> None:
        run_stream = await async_client.beta.threads.runs.submit_tool_outputs(
            "string",
            thread_id="string",
            stream=True,
            tool_outputs=[{}],
        )
        await run_stream.response.aclose()

    @parametrize
    async def test_raw_response_submit_tool_outputs_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
            "string",
            thread_id="string",
            stream=True,
            tool_outputs=[{}],
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_submit_tool_outputs_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.submit_tool_outputs(
            "string",
            thread_id="string",
            stream=True,
            tool_outputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_tool_outputs_overload_2(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "string",
                thread_id="",
                stream=True,
                tool_outputs=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "",
                thread_id="string",
                stream=True,
                tool_outputs=[{}],
            )


================================================
File: /tests/api_resources/beta/realtime/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/beta/realtime/test_sessions.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types.beta.realtime import SessionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        session = client.beta.realtime.sessions.create(
            model="gpt-4o-realtime-preview",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        session = client.beta.realtime.sessions.create(
            model="gpt-4o-realtime-preview",
            input_audio_format="pcm16",
            input_audio_transcription={"model": "model"},
            instructions="instructions",
            max_response_output_tokens=0,
            modalities=["text"],
            output_audio_format="pcm16",
            temperature=0,
            tool_choice="tool_choice",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {},
                    "type": "function",
                }
            ],
            turn_detection={
                "create_response": True,
                "prefix_padding_ms": 0,
                "silence_duration_ms": 0,
                "threshold": 0,
                "type": "type",
            },
            voice="alloy",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.realtime.sessions.with_raw_response.create(
            model="gpt-4o-realtime-preview",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.realtime.sessions.with_streaming_response.create(
            model="gpt-4o-realtime-preview",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        session = await async_client.beta.realtime.sessions.create(
            model="gpt-4o-realtime-preview",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        session = await async_client.beta.realtime.sessions.create(
            model="gpt-4o-realtime-preview",
            input_audio_format="pcm16",
            input_audio_transcription={"model": "model"},
            instructions="instructions",
            max_response_output_tokens=0,
            modalities=["text"],
            output_audio_format="pcm16",
            temperature=0,
            tool_choice="tool_choice",
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {},
                    "type": "function",
                }
            ],
            turn_detection={
                "create_response": True,
                "prefix_padding_ms": 0,
                "silence_duration_ms": 0,
                "threshold": 0,
                "type": "type",
            },
            voice="alloy",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.realtime.sessions.with_raw_response.create(
            model="gpt-4o-realtime-preview",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.realtime.sessions.with_streaming_response.create(
            model="gpt-4o-realtime-preview",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/beta/vector_stores/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/beta/vector_stores/test_files.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta.vector_stores import (
    VectorStoreFile,
    VectorStoreFileDeleted,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        file = client.beta.vector_stores.files.create(
            "vs_abc123",
            file_id="string",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        file = client.beta.vector_stores.files.create(
            "vs_abc123",
            file_id="string",
            chunking_strategy={"type": "auto"},
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.files.with_raw_response.create(
            "vs_abc123",
            file_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.vector_stores.files.with_streaming_response.create(
            "vs_abc123",
            file_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.files.with_raw_response.create(
                "",
                file_id="string",
            )

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        file = client.beta.vector_stores.files.retrieve(
            "file-abc123",
            vector_store_id="vs_abc123",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.files.with_raw_response.retrieve(
            "file-abc123",
            vector_store_id="vs_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.vector_stores.files.with_streaming_response.retrieve(
            "file-abc123",
            vector_store_id="vs_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.files.with_raw_response.retrieve(
                "file-abc123",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.beta.vector_stores.files.with_raw_response.retrieve(
                "",
                vector_store_id="vs_abc123",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        file = client.beta.vector_stores.files.list(
            "string",
        )
        assert_matches_type(SyncCursorPage[VectorStoreFile], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        file = client.beta.vector_stores.files.list(
            "string",
            after="string",
            before="string",
            filter="in_progress",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[VectorStoreFile], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.files.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncCursorPage[VectorStoreFile], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.beta.vector_stores.files.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncCursorPage[VectorStoreFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.files.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        file = client.beta.vector_stores.files.delete(
            "string",
            vector_store_id="string",
        )
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.files.with_raw_response.delete(
            "string",
            vector_store_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.beta.vector_stores.files.with_streaming_response.delete(
            "string",
            vector_store_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.files.with_raw_response.delete(
                "string",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.beta.vector_stores.files.with_raw_response.delete(
                "",
                vector_store_id="string",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.beta.vector_stores.files.create(
            "vs_abc123",
            file_id="string",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.beta.vector_stores.files.create(
            "vs_abc123",
            file_id="string",
            chunking_strategy={"type": "auto"},
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.files.with_raw_response.create(
            "vs_abc123",
            file_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.files.with_streaming_response.create(
            "vs_abc123",
            file_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.files.with_raw_response.create(
                "",
                file_id="string",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.beta.vector_stores.files.retrieve(
            "file-abc123",
            vector_store_id="vs_abc123",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.files.with_raw_response.retrieve(
            "file-abc123",
            vector_store_id="vs_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.files.with_streaming_response.retrieve(
            "file-abc123",
            vector_store_id="vs_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.files.with_raw_response.retrieve(
                "file-abc123",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.beta.vector_stores.files.with_raw_response.retrieve(
                "",
                vector_store_id="vs_abc123",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.beta.vector_stores.files.list(
            "string",
        )
        assert_matches_type(AsyncCursorPage[VectorStoreFile], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.beta.vector_stores.files.list(
            "string",
            after="string",
            before="string",
            filter="in_progress",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[VectorStoreFile], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.files.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(AsyncCursorPage[VectorStoreFile], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.files.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncCursorPage[VectorStoreFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.files.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenAI) -> None:
        file = await async_client.beta.vector_stores.files.delete(
            "string",
            vector_store_id="string",
        )
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.files.with_raw_response.delete(
            "string",
            vector_store_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.files.with_streaming_response.delete(
            "string",
            vector_store_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.files.with_raw_response.delete(
                "string",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.beta.vector_stores.files.with_raw_response.delete(
                "",
                vector_store_id="string",
            )


================================================
File: /tests/api_resources/beta/vector_stores/test_file_batches.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta.vector_stores import (
    VectorStoreFile,
    VectorStoreFileBatch,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        file_batch = client.beta.vector_stores.file_batches.create(
            "vs_abc123",
            file_ids=["string"],
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        file_batch = client.beta.vector_stores.file_batches.create(
            "vs_abc123",
            file_ids=["string"],
            chunking_strategy={"type": "auto"},
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.file_batches.with_raw_response.create(
            "vs_abc123",
            file_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.vector_stores.file_batches.with_streaming_response.create(
            "vs_abc123",
            file_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.create(
                "",
                file_ids=["string"],
            )

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        file_batch = client.beta.vector_stores.file_batches.retrieve(
            "vsfb_abc123",
            vector_store_id="vs_abc123",
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.file_batches.with_raw_response.retrieve(
            "vsfb_abc123",
            vector_store_id="vs_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.vector_stores.file_batches.with_streaming_response.retrieve(
            "vsfb_abc123",
            vector_store_id="vs_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.retrieve(
                "vsfb_abc123",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.retrieve(
                "",
                vector_store_id="vs_abc123",
            )

    @parametrize
    def test_method_cancel(self, client: OpenAI) -> None:
        file_batch = client.beta.vector_stores.file_batches.cancel(
            "string",
            vector_store_id="string",
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.file_batches.with_raw_response.cancel(
            "string",
            vector_store_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: OpenAI) -> None:
        with client.beta.vector_stores.file_batches.with_streaming_response.cancel(
            "string",
            vector_store_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.cancel(
                "string",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.cancel(
                "",
                vector_store_id="string",
            )

    @parametrize
    def test_method_list_files(self, client: OpenAI) -> None:
        file_batch = client.beta.vector_stores.file_batches.list_files(
            "string",
            vector_store_id="string",
        )
        assert_matches_type(SyncCursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    def test_method_list_files_with_all_params(self, client: OpenAI) -> None:
        file_batch = client.beta.vector_stores.file_batches.list_files(
            "string",
            vector_store_id="string",
            after="string",
            before="string",
            filter="in_progress",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    def test_raw_response_list_files(self, client: OpenAI) -> None:
        response = client.beta.vector_stores.file_batches.with_raw_response.list_files(
            "string",
            vector_store_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(SyncCursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    def test_streaming_response_list_files(self, client: OpenAI) -> None:
        with client.beta.vector_stores.file_batches.with_streaming_response.list_files(
            "string",
            vector_store_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(SyncCursorPage[VectorStoreFile], file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_files(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.list_files(
                "string",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.beta.vector_stores.file_batches.with_raw_response.list_files(
                "",
                vector_store_id="string",
            )


class TestAsyncFileBatches:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        file_batch = await async_client.beta.vector_stores.file_batches.create(
            "vs_abc123",
            file_ids=["string"],
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        file_batch = await async_client.beta.vector_stores.file_batches.create(
            "vs_abc123",
            file_ids=["string"],
            chunking_strategy={"type": "auto"},
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.file_batches.with_raw_response.create(
            "vs_abc123",
            file_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.file_batches.with_streaming_response.create(
            "vs_abc123",
            file_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.create(
                "",
                file_ids=["string"],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        file_batch = await async_client.beta.vector_stores.file_batches.retrieve(
            "vsfb_abc123",
            vector_store_id="vs_abc123",
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.file_batches.with_raw_response.retrieve(
            "vsfb_abc123",
            vector_store_id="vs_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.file_batches.with_streaming_response.retrieve(
            "vsfb_abc123",
            vector_store_id="vs_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.retrieve(
                "vsfb_abc123",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.retrieve(
                "",
                vector_store_id="vs_abc123",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpenAI) -> None:
        file_batch = await async_client.beta.vector_stores.file_batches.cancel(
            "string",
            vector_store_id="string",
        )
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.file_batches.with_raw_response.cancel(
            "string",
            vector_store_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.file_batches.with_streaming_response.cancel(
            "string",
            vector_store_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(VectorStoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.cancel(
                "string",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.cancel(
                "",
                vector_store_id="string",
            )

    @parametrize
    async def test_method_list_files(self, async_client: AsyncOpenAI) -> None:
        file_batch = await async_client.beta.vector_stores.file_batches.list_files(
            "string",
            vector_store_id="string",
        )
        assert_matches_type(AsyncCursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    async def test_method_list_files_with_all_params(self, async_client: AsyncOpenAI) -> None:
        file_batch = await async_client.beta.vector_stores.file_batches.list_files(
            "string",
            vector_store_id="string",
            after="string",
            before="string",
            filter="in_progress",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    async def test_raw_response_list_files(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.vector_stores.file_batches.with_raw_response.list_files(
            "string",
            vector_store_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(AsyncCursorPage[VectorStoreFile], file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_list_files(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.vector_stores.file_batches.with_streaming_response.list_files(
            "string",
            vector_store_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(AsyncCursorPage[VectorStoreFile], file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_files(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.list_files(
                "string",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.beta.vector_stores.file_batches.with_raw_response.list_files(
                "",
                vector_store_id="string",
            )


================================================
File: /tests/api_resources/beta/test_threads.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.types.beta import (
    Thread,
    ThreadDeleted,
)
from openai.types.beta.threads import Run

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestThreads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        thread = client.beta.threads.create()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        thread = client.beta.threads.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {},
                }
            ],
            metadata={},
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {
                    "vector_store_ids": ["string"],
                    "vector_stores": [
                        {
                            "chunking_strategy": {"type": "auto"},
                            "file_ids": ["string"],
                            "metadata": {},
                        }
                    ],
                },
            },
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        thread = client.beta.threads.retrieve(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.threads.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.threads.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: OpenAI) -> None:
        thread = client.beta.threads.update(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: OpenAI) -> None:
        thread = client.beta.threads.update(
            "string",
            metadata={},
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: OpenAI) -> None:
        response = client.beta.threads.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: OpenAI) -> None:
        with client.beta.threads.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        thread = client.beta.threads.delete(
            "string",
        )
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.beta.threads.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI) -> None:
        with client.beta.threads.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(ThreadDeleted, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_and_run_overload_1(self, client: OpenAI) -> None:
        thread = client.beta.threads.create_and_run(
            assistant_id="string",
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    def test_method_create_and_run_with_all_params_overload_1(self, client: OpenAI) -> None:
        thread = client.beta.threads.create_and_run(
            assistant_id="string",
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            stream=False,
            temperature=1,
            thread={
                "messages": [
                    {
                        "content": "string",
                        "role": "user",
                        "attachments": [
                            {
                                "file_id": "file_id",
                                "tools": [{"type": "code_interpreter"}],
                            }
                        ],
                        "metadata": {},
                    }
                ],
                "metadata": {},
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["string"]},
                    "file_search": {
                        "vector_store_ids": ["string"],
                        "vector_stores": [
                            {
                                "chunking_strategy": {"type": "auto"},
                                "file_ids": ["string"],
                                "metadata": {},
                            }
                        ],
                    },
                },
            },
            tool_choice="none",
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    def test_raw_response_create_and_run_overload_1(self, client: OpenAI) -> None:
        response = client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    def test_streaming_response_create_and_run_overload_1(self, client: OpenAI) -> None:
        with client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = response.parse()
            assert_matches_type(Run, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_and_run_overload_2(self, client: OpenAI) -> None:
        thread_stream = client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
        )
        thread_stream.response.close()

    @parametrize
    def test_method_create_and_run_with_all_params_overload_2(self, client: OpenAI) -> None:
        thread_stream = client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            temperature=1,
            thread={
                "messages": [
                    {
                        "content": "string",
                        "role": "user",
                        "attachments": [
                            {
                                "file_id": "file_id",
                                "tools": [{"type": "code_interpreter"}],
                            }
                        ],
                        "metadata": {},
                    }
                ],
                "metadata": {},
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["string"]},
                    "file_search": {
                        "vector_store_ids": ["string"],
                        "vector_stores": [
                            {
                                "chunking_strategy": {"type": "auto"},
                                "file_ids": ["string"],
                                "metadata": {},
                            }
                        ],
                    },
                },
            },
            tool_choice="none",
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        thread_stream.response.close()

    @parametrize
    def test_raw_response_create_and_run_overload_2(self, client: OpenAI) -> None:
        response = client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_and_run_overload_2(self, client: OpenAI) -> None:
        with client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncThreads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.create()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.create(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "attachments": [
                        {
                            "file_id": "file_id",
                            "tools": [{"type": "code_interpreter"}],
                        }
                    ],
                    "metadata": {},
                }
            ],
            metadata={},
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {
                    "vector_store_ids": ["string"],
                    "vector_stores": [
                        {
                            "chunking_strategy": {"type": "auto"},
                            "file_ids": ["string"],
                            "metadata": {},
                        }
                    ],
                },
            },
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.retrieve(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.update(
            "string",
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.update(
            "string",
            metadata={},
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
        )
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Thread, thread, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Thread, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.delete(
            "string",
        )
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(ThreadDeleted, thread, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(ThreadDeleted, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_and_run_overload_1(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.create_and_run(
            assistant_id="string",
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    async def test_method_create_and_run_with_all_params_overload_1(self, async_client: AsyncOpenAI) -> None:
        thread = await async_client.beta.threads.create_and_run(
            assistant_id="string",
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            stream=False,
            temperature=1,
            thread={
                "messages": [
                    {
                        "content": "string",
                        "role": "user",
                        "attachments": [
                            {
                                "file_id": "file_id",
                                "tools": [{"type": "code_interpreter"}],
                            }
                        ],
                        "metadata": {},
                    }
                ],
                "metadata": {},
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["string"]},
                    "file_search": {
                        "vector_store_ids": ["string"],
                        "vector_stores": [
                            {
                                "chunking_strategy": {"type": "auto"},
                                "file_ids": ["string"],
                                "metadata": {},
                            }
                        ],
                    },
                },
            },
            tool_choice="none",
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    async def test_raw_response_create_and_run_overload_1(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        thread = response.parse()
        assert_matches_type(Run, thread, path=["response"])

    @parametrize
    async def test_streaming_response_create_and_run_overload_1(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            thread = await response.parse()
            assert_matches_type(Run, thread, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_and_run_overload_2(self, async_client: AsyncOpenAI) -> None:
        thread_stream = await async_client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
        )
        await thread_stream.response.aclose()

    @parametrize
    async def test_method_create_and_run_with_all_params_overload_2(self, async_client: AsyncOpenAI) -> None:
        thread_stream = await async_client.beta.threads.create_and_run(
            assistant_id="string",
            stream=True,
            instructions="string",
            max_completion_tokens=256,
            max_prompt_tokens=256,
            metadata={},
            model="gpt-4o",
            parallel_tool_calls=True,
            response_format="auto",
            temperature=1,
            thread={
                "messages": [
                    {
                        "content": "string",
                        "role": "user",
                        "attachments": [
                            {
                                "file_id": "file_id",
                                "tools": [{"type": "code_interpreter"}],
                            }
                        ],
                        "metadata": {},
                    }
                ],
                "metadata": {},
                "tool_resources": {
                    "code_interpreter": {"file_ids": ["string"]},
                    "file_search": {
                        "vector_store_ids": ["string"],
                        "vector_stores": [
                            {
                                "chunking_strategy": {"type": "auto"},
                                "file_ids": ["string"],
                                "metadata": {},
                            }
                        ],
                    },
                },
            },
            tool_choice="none",
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
            truncation_strategy={
                "type": "auto",
                "last_messages": 1,
            },
        )
        await thread_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_and_run_overload_2(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.with_raw_response.create_and_run(
            assistant_id="string",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_and_run_overload_2(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.with_streaming_response.create_and_run(
            assistant_id="string",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True


================================================
File: /tests/api_resources/beta/__init__.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


================================================
File: /tests/api_resources/beta/test_assistants.py
================================================
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta import (
    Assistant,
    AssistantDeleted,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssistants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.create(
            model="gpt-4o",
        )
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.create(
            model="gpt-4o",
            description="description",
            instructions="instructions",
            metadata={},
            name="name",
            response_format="auto",
            temperature=1,
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {
                    "vector_store_ids": ["string"],
                    "vector_stores": [
                        {
                            "chunking_strategy": {"type": "auto"},
                            "file_ids": ["string"],
                            "metadata": {},
                        }
                    ],
                },
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
        )
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.assistants.with_raw_response.create(
            model="gpt-4o",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.assistants.with_streaming_response.create(
            model="gpt-4o",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(Assistant, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.retrieve(
            "assistant_id",
        )
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.assistants.with_raw_response.retrieve(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.assistants.with_streaming_response.retrieve(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(Assistant, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.beta.assistants.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.update(
            assistant_id="assistant_id",
        )
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.update(
            assistant_id="assistant_id",
            description="description",
            instructions="instructions",
            metadata={},
            model="model",
            name="name",
            response_format="auto",
            temperature=1,
            tool_resources={
                "code_interpreter": {"file_ids": ["string"]},
                "file_search": {"vector_store_ids": ["string"]},
            },
            tools=[{"type": "code_interpreter"}],
            top_p=1,
        )
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: OpenAI) -> None:
        response = client.beta.assistants.with_raw_response.update(
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(Assistant, assistant, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: OpenAI) -> None:
        with client.beta.assistants.with_streaming_response.update(
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(Assistant, assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.beta.assistants.with_raw_response.update(
                assistant_id="",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.list()
        assert_matches_type(SyncCursorPage[Assistant], assistant, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.list(
            after="after",
            before="before",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[Assistant], assistant, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.beta.assistants.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(SyncCursorPage[Assistant], assistant, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.beta.assistants.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assistant = response.parse()
            assert_matches_type(SyncCursorPage[Assistant], assistant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: OpenAI) -> None:
        assistant = client.beta.assistants.delete(
            "assistant_id",
        )
        assert_matches_type(AssistantDeleted, assistant, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: OpenAI) -> None:
        response = client.beta.assistants.with_raw_response.delete(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assistant = response.parse()
        assert_matches_type(AssistantDeleted, assistant, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: OpenAI)