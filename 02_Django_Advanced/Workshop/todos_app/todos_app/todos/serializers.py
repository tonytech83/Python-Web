from rest_framework import serializers

from todos_app.todos.models import Todo, Category, TodoState


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoListSerializer(TodoBaseSerializer):
    category = CategorySerializer(many=False)


class TodoDetailSerializer(TodoBaseSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)

        result['is_done'] = result['state'] == TodoState.DONE

        return result


class TodoCreateSerializer(TodoBaseSerializer):
    class Meta(TodoBaseSerializer.Meta):
        fields = ('title', 'description', 'category')

    # Assigned Todo to use who call `ADD TODO` button
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data)

    # NOT NEEDED
    # def create(self, validated_data):
    #     # receive object
    #     category_data = validated_data.pop('category')
    #
    #     # create new `category`
    #     category, is_created = Category.objects.get_or_create(**category_data)
    #
    #     # create `todo` with `category`
    #     return Todo.objects.create(**validated_data, category=category)
